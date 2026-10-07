"""
This is upgrade version of classify_ticket_v2 from P05
In P05 we were quering the table directly and getting all the complaints or using the limit, but for frontend that will not work
so we use fastapi services, we will pass the contract id and agency id to get the complaint and than pass the complaint to llm
This is to get full view, urgency, sentiment, analyze, suggested actions etc

Instead of running from the inside we can run it from parent folder
uv run fastapi dev P06_SmartOps_FastAPI/classify_ticket_v3.py

I am also adding pydantic validators from week 11 in this project
for custom error as we are using router, the error will be placed inside the main file where fastapi , app is there
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from P06_SmartOps_FastAPI.supabase_client import get_supabase_client
from P05_SmartOps_AI_Operations import classify_ticket_v2

router = APIRouter()

class ClassifyTicketRequest(BaseModel):
    complaint_id : str
    agency_id : str
    contract_id : str
    """
    if we do not write mode the default mode is after
    also we used three fields in field validator : Pydantic runs the same validator separately for each one.
    we use strip and not just value because : strip() removes spaces from the beginning and end of a string
    """
    @field_validator("complaint_id", "agency_id", "contract_id")
    @classmethod
    def cannot_be_empty(cls, value: str) -> str:
        if not value.strip():
          raise ValueError("Field cannot be empty")
          """
          if this error hits it will redirect to RequestValidationError which is custom handled in main.py
          see both the example below, if its handled custom or standard
          """
        return value 

@router.post("/api/v1/classify_ticket")
def classify_ticket_endpoint(request : ClassifyTicketRequest):
    """
    Input request body has to follow the pydantic structure
    """

    """
    below agency id is just for raising global code error handler in main.y : line  51 and 52
    """
    if request.agency_id == "trigger500":
        raise RuntimeError("Testing global 500 Handler")
    
    supabase = get_supabase_client()

    response = (
        supabase
        .table("complaints")
        .select("id, description, agency_id")
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

    result = classify_ticket_v2.classify_ticket_v2(complaint_text)

    return result

"""
This will be thee error message if we do not have custom error handler
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "complaint_id"
      ],
      "msg": "Value error, Field cannot be empty",
      "input": "",
      "ctx": {
        "error": {}
      }
    },
    {
      "type": "value_error",
      "loc": [
        "body",
        "agency_id"
      ],
      "msg": "Value error, Field cannot be empty",
      "input": " ",
      "ctx": {
        "error": {}
      }
    },
    {
      "type": "value_error",
      "loc": [
        "body",
        "contract_id"
      ],
      "msg": "Value error, Field cannot be empty",
      "input": "",
      "ctx": {
        "error": {}
      }
    }
  ]
}
"""

"""
After custom error , validation error will be 
{
  "errors": [
    {
      "field": "complaint_id",
      "error": "value_error",
      "message": "Value error, Field cannot be empty"
    },
    {
      "field": "agency_id",
      "error": "value_error",
      "message": "Value error, Field cannot be empty"
    },
    {
      "field": "contract_id",
      "error": "value_error",
      "message": "Value error, Field cannot be empty"
    }
  ]
}
"""