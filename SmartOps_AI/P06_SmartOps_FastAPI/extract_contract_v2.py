"""
this is the upgrade version of extract contract
In this we use fatsapi endpoints to call the llm and pass the necessary ids
this will just sumarize the contract, give renewal score, with details and it will need all the info from survey, incident, complaints

I am also adding pydantic validators annotated type from week 11 in this project
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, AfterValidator

from typing import Annotated

from P06_SmartOps_FastAPI.supabase_client import get_supabase_client
from P05_SmartOps_AI_Operations import extract_contract_data

router = APIRouter()

def not_empty(value : str) -> str:
    value = value.strip()

    if not value:
        raise ValueError("Field cannot be empty")
    
    return value

NonEmptyString = Annotated[str, AfterValidator(not_empty)]

class ContractDetailRequest(BaseModel):
    contract_id : NonEmptyString
    agency_id : NonEmptyString

    """
    we can also write like this , choose whichever makes you comfortable
    contract_id : Annotated[str, AfterValidator(not_empty)]
    agency_id : Annotated[str, AfterValidator(not_empty)]
    """

@router.post("/api/v1/contract_data")
def contract_data_endpoint(request : ContractDetailRequest):
    
    supabase = get_supabase_client()

    """
    Now here our llm is taking two parameters, one is contract data
    second one is other details which consists of complaints, surveys and incidents
    """

    contract_response = (
        supabase
        .table("contracts")
        .select("*")
        .eq("id", request.contract_id)
        .eq("agency_id", request.agency_id)
        .limit(1)
        .execute()
    )

    if not contract_response.data:
        raise HTTPException(
            status_code=404,
            detail="Contract Not Found"
        )

    contract = contract_response.data[0]

    complaint_response = (
        supabase
        .table("complaints")
        .select("*")
        .eq("contract_id", request.contract_id)
        .eq("agency_id", request.agency_id)
        .execute()
    )

    survey_response = (
        supabase
        .table("surveys")
        .select("*")
        .eq("contract_id", request.contract_id)
        .eq("agency_id", request.agency_id)
        .execute()
    )

    incident_response = (
        supabase
        .table("incidents")
        .select("*")
        .eq("contract_id", request.contract_id)
        .eq("agency_id", request.agency_id)
        .execute()
    )

    other_details = {
        "surveys" : survey_response.data,
        "complaints" : complaint_response.data,
        "incidents" : incident_response.data
    }

    result = extract_contract_data.contract_data(contract, other_details)
    return result