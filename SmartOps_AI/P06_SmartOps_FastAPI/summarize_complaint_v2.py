"""
this is the upgrade version of summarize complaint
In this we use fatsapi endpoints to call the llm and pass the necessary ids
this will just sumarize the complaint and tell the urgency
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from P06_SmartOps_FastAPI.supabase_client import get_supabase_client
from P05_SmartOps_AI_Operations import summarize_complaint

router = APIRouter()

class SummarizeComplaintRequest(BaseModel):
    complaint_id : str
    agency_id : str
    contract_id : str

    @field_validator("complaint_id", "agency_id", "contract_id")
    @classmethod
    def cannot_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value 

@router.post("/api/v1/summarize_complaint")
def summarize_complaint_endpoint(request : SummarizeComplaintRequest):
    supabase = get_supabase_client()

    response = (
        supabase
        .table("complaints")
        .select("id", "description", "agency_id")
        .eq("id", request.complaint_id)
        .eq("agency_id", request.agency_id)
        .eq("contract_id", request.contract_id)
        .limit(1)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code = 404,
            detail = "Complaint Not Found"
        )

    complaint = response.data[0]
    complaint_text = complaint["description"]

    result = summarize_complaint.summarize_complaint(complaint_text)
    return result
    