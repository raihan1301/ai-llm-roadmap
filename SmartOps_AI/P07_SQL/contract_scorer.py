from anthropic import AnthropicBedrock
from botocore.config import Config
from pydantic import (BaseModel, Field,  field_validator)
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

import boto3
import json
import time

from P06_SmartOps_FastAPI.supabase_client import get_supabase_client
from P07_SQL.AI_Log import (SessionDep, log_ai_call, AILogCreate)

router = APIRouter()

"""
System Prompt
"""
def prompt(contract_details, other_details):
    system_prompt = f"""
        Your are SmartOps Contract Renewal Scorer Analyze Agent.

        Step 1: 
        From {contract_details} extract important information of contract.
        you should extract start date, end date, renewal happened, payment terms, Extract other important information as well

        Step 2:
        from {other_details} extract related information for contracts
        How many complaints are recieved from client during this contract, is it resolved or not,
        How many Surveys are recieved from client, what are the NPS score of that, 
            If client is agnry on survey , is there any steps taken to resolve it.
        How many incidents happened during this contract terms and does it resolved.

        Step 3:
        After Analyzing all the information you have from {contract_details} and {other_details} calculate the risk score
        risk score will indicate if the client will going to renew his contract or not
        0 : means client will definetly going to renew the contract
        10 : means client will not renew

        Step 4:
        After that do the reasoning, why you have given this score and give the valid reason justifying your risk score

        Step 5:
        Suggest action that can be taken to redecue the Risk Score
        for example if the survey is bad giving some gift cards or giving discount on next contract can help them stay.
            If they are angry because of complaints or incidents, than giving better service next time
        so suggest what can be the next steps

        Do not invent your own information. all the info should come from the text given to you
        If you are suggesting the next actions its should be relevant to the reason you provided
        Do not miss any important information.
        do not suggest any action has already been started.
        If you dont know anything output "Dont know" for that particular thing
    """
    return system_prompt


"""
Output BaseModel Class
"""
class ContractRiskResult(BaseModel):
    contract_id : str
    risk_score : int = Field(ge=1, le=10)
    reasoning : str
    suggested_action : str


"""
Input BaseModel Class
"""
class ContractRisk(BaseModel):
    agency_id : str
    contract_id : str

    @field_validator("agency_id", "contract_id")
    @classmethod
    def cannot_be_empty(cls, value : str) -> str:
        if not value.strip():
            raise ValueError("Field Cannot be Empty")
        else:
            return value


"""
Call Supabase to get the data from contract, incident, survey, complaints
"""
def contract_supabase_data(agency_id : str, contract_id : str):

    supabase = get_supabase_client()

    contract_response = (
        supabase
        .table("contracts")
        .select("*")
        .eq("id", contract_id)
        .eq("agency_id", agency_id)
        .limit(1)
        .execute()
    )
    
    if not contract_response.data:
        raise HTTPException(
            status_code=404,
            detail="Contract Not Found"
        )
    
    contract_details = contract_response.data[0]

    complaint_response = (
        supabase
        .table("complaints")
        .select("*")
        .eq("contract_id", contract_id)
        .eq("agency_id", agency_id)
        .execute()
    )
    
    survey_response = (
        supabase
        .table("surveys")
        .select("*")
        .eq("contract_id", contract_id)
        .eq("agency_id", agency_id)
        .execute()
    )
    
    incident_response = (
        supabase
        .table("incidents")
        .select("*")
        .eq("contract_id", contract_id)
        .eq("agency_id", agency_id)
        .execute()
    )
    
    other_details = {
        "surveys" : survey_response.data,
        "complaints" : complaint_response.data,
        "incidents" : incident_response.data
    }

    return contract_details, other_details


"""
We also have to log the LLM Model metrics
"""
class LLMMetrics(BaseModel):
    model_used : str
    input_tokens : int
    output_tokens : int
    total_tokens : int


"""
calling LLM to work on it
"""
def Contract_Risk_LLM(contract_details, other_details):
    
    system_prompt = prompt(contract_details, other_details)

    session = boto3.Session()
    AWS_REGION = session.region_name
    MODEL_NAME = "us.anthropic.claude-sonnet-4-6"

    client = AnthropicBedrock(aws_region=AWS_REGION)

    content = f"""
        CONTRACT : {json.dumps(contract_details, indent=2)}
    
        RELATED INFORMATION : {json.dumps(other_details, indent=2)}
    """

    response = client.messages.parse(
         model = MODEL_NAME,
        max_tokens = 20000,
        system = system_prompt,
        messages = [
            {
                "role" : "user",
                "content" : content
            }
        ],
        output_format=ContractRiskResult
    )

    result = response.parsed_output

    metrics = LLMMetrics(
        model_used = response.model,
        input_tokens = response.usage.input_tokens,
        output_tokens = response.usage.output_tokens,
        total_tokens = (response.usage.input_tokens + response.usage.output_tokens)
    )

    return result, metrics


"""
calculate cost function
"""
def calculate_cost(input_tokens : int, output_tokens :  int) -> float:
    input_cost = (input_tokens / 1000000) * 3.00
    output_cost = (output_tokens / 1000000) * 15.00

    return input_cost + output_cost


"""
Call LLM from here via endpoint,
"""
@router.post("/api/v1/contract_riskscorer")
def contract_risk_endpoint(request : ContractRisk, session : SessionDep):
    start_time = time.perf_counter()

    contract_details , other_details = contract_supabase_data(
        agency_id = request.agency_id,
        contract_id = request.contract_id
    )

    result, metrics = Contract_Risk_LLM(
        contract_details = contract_details,
        other_details = other_details
    )

    end_time = time.perf_counter()

    latency_ms = (end_time - start_time) * 1000
    cost_usd = calculate_cost(metrics.input_tokens, metrics.output_tokens)

    """
    we will fill input base model for Ai Log and than call the sql model
    """
    log_data = AILogCreate(
        endpoint = "/api/v1/contract_riskscorer",
        agency_id = request.agency_id,

        input_preview = f"Contract ID : {request.contract_id}",
        output_json = result.model_dump_json(),

        model_used = metrics.model_used,

        cost_usd = cost_usd,
        token_used = metrics.total_tokens,
        latency_ms = latency_ms
    )

    """
    now we call sql model to update database
    """
    log_ai_call(
        session = session,
        log_data = log_data
    )

    return result