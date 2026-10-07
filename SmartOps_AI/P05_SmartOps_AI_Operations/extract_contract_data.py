"""
contract_id
    ↓
Supabase contracts table
    ↓
Get contract record/content
    ↓
If missing → valid=False
    ↓
Claude extracts important contract information
    ↓
Structured Pydantic response
"""

from supabase import create_client
from dotenv import load_dotenv
import json
from pydantic import BaseModel
from anthropic import AnthropicBedrock
import os
import boto3

"""
This is the pydantic structure for model LLM
"""
class ContractSummaryAI(BaseModel):
    start_date: str
    end_date: str
    contract_value: str
    renewal_terms: str
    payment_terms: str
    complaints: int
    survey: str
    incident : int
    renewal_score : int
    renewal_score_reason : str
    other_information : str

"""
This will be final output structure include all the values
"""
class ContractSummary(BaseModel):
    valid: bool
    contract_id: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    contract_value: str | None = None
    renewal_terms: str | None = None
    payment_terms: str | None = None
    complaints: int | None = None
    survey: str | None = None
    incident : int | None = None
    renewal_score : int | None = None
    renewal_score_reason : str | None = None
    other_information : str | None = None
    reason: str | None = None

"""
This method will extract important information from contract, it will recieve contract details as parameter
"""
def contract_data(contract_details, other_details):

    system_prompt = f"""
    You are SmartOps Contract data Extractor.

    Your job is to extract important information from the contract and do the following steps mentioned below
    Step 1:
        from {contract_details} extract important contract information. 
        you should extract contract start date, end date, contract value, payment terms, renewal terms
        you should also extract any other important information you found in contract_details
        
    Step 2:
        we also provided you with {other_details} : this contains if there is any survey, incident, complaints related to this contract
        analyze the details and extract how many complaints are recieved for this contract
        extract how many incidents occur in this contract : it will count in this contract, if incident date is between contract start and end date
        extract all the survey related to this contract, count them, analyze their sentiment and average out what is the overal sentiment
    
    Step 3:
        One you process all the information , analyze what can be the renewal score for this contract.
        0 - they will not going to renew it
        10 - they will definetly going to renew the contract
        Also describe the reason why you gave this renewal score to this contract

    Do not invent your own information. all the info should come from the text given to you
    Do not miss any important information.
    do not suggest any action has already been started.
    If you dont know anything output "Dont know" for that particular thing
    """

    content = f"""
    CONTRACT : {json.dumps(contract_details, indent=2)}

    RELATED INFORMATION : {json.dumps(other_details, indent=2)}
    """

    session = boto3.Session() # create a boto3 session to dynamically get and set the region name
    AWS_REGION = session.region_name
    MODEL_NAME = "us.anthropic.claude-sonnet-4-6"
    
    client = AnthropicBedrock(aws_region=AWS_REGION)
        
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
        output_format=ContractSummaryAI
    )
    
    return response.parsed_output


"""
This method will get the contract from supabase
"""
def get_contract(contract_id):
    load_dotenv()
        
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
        
    response = (
        supabase
        .table("contracts")
        .select("*")
        .eq("id", contract_id)
        .maybe_single()
        .execute()
    )

    contract = response.data

    if not contract:
        return None

    return contract

"""
This will get other information for that contract
"""
def get_other_details(contract_id):
    load_dotenv()
        
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
        
    survey_response = (
        supabase
        .table("surveys")
        .select("*")
        .eq("contract_id", contract_id)
        .execute()
    )

    complaint_response = (
        supabase
        .table("complaints")
        .select("*")
        .eq("contract_id", contract_id)
        .execute()
    )

    incident_response = (
        supabase
        .table("incidents")
        .select("*")
        .eq("contract_id", contract_id)
        .execute()
    )

    return {
        "surveys" : survey_response.data,
        "complaints" : complaint_response.data,
        "incidents" : incident_response.data
    }


def main():
    contract_id = input("Enter Contract id : ")
    """
    right now it is by terminal, in smartops we can automate that, as soon as complaint lands
    or user click button it will fetch the complaint id, for testing we are using input mechanism now
    """

    contract_description = get_contract(contract_id)
    print("\n contract_description:")
    print(contract_description)

    if not contract_description:
        result = ContractSummary(
            valid=False,
            contract_id=contract_id,
            reason="contract not found."
        )

    else:
        other_details = get_other_details(contract_id)
        print("\n other_details:")
        print(other_details)

        contract_data_extraction = contract_data(contract_details=contract_description, other_details=other_details)

        result = ContractSummary(
            valid=True,
            contract_id=contract_id,
            start_date=contract_data_extraction.start_date,
            end_date=contract_data_extraction.end_date,
            contract_value=contract_data_extraction.contract_value,
            renewal_terms=contract_data_extraction.renewal_terms,
            payment_terms=contract_data_extraction.payment_terms,
            complaints=contract_data_extraction.complaints,
            survey=contract_data_extraction.survey,
            incident=contract_data_extraction.incident,
            renewal_score=contract_data_extraction.renewal_score,
            renewal_score_reason=contract_data_extraction.renewal_score_reason,
            other_information=contract_data_extraction.other_information
        )

    contract_json = json.dumps(result.model_dump(mode="json"),indent = 4)

    print("\n AI Result:")
    print(contract_json)


if __name__ == "__main__":
        main()

