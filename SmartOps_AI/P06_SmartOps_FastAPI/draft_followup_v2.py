"""
this is the upgrade version of draft followup
In this we use fatsapi endpoints to call the llm and pass the necessary ids
this will just give type of followup, email subject and body

I am also adding pydantic validators from week 11 in this project
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
from typing import Any

from P06_SmartOps_FastAPI.supabase_client import get_supabase_client
from P05_SmartOps_AI_Operations import draft_followup

router = APIRouter()

class DraftFollowupRequest(BaseModel):
    contract_id : str
    agency_id : str
    
    """
    This file use the before mode, classify_ticket_v3 used after mode
    """
    @field_validator("contract_id", "agency_id", mode="before")
    @classmethod
    def clean_and_validate(cls, value : Any) -> Any:
        if isinstance(value, str):
            value = value.strip()

            if not value:
                raise ValueError("field cannot be empty")
        return value


@router.post("/api/v1/draft_followup")
def draft_followup_endpoint(request : DraftFollowupRequest):
    supabase = get_supabase_client()

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

    result = draft_followup.followup_draft_email(contract, other_details)
    return result
   