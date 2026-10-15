"""
This is upgrade version of classify_ticket_v2 from P05
In P05 we were quering the table directly and getting all the complaints or using the limit, but for frontend that will not work
so we use fastapi services, we will pass the contract id and agency id to get the complaint and than pass the complaint to llm
This is to get full view, urgency, sentiment, analyze, suggested actions etc

Instead of running from the inside we can run it from parent folder
uv run fastapi dev P06_SmartOps_FastAPI/classify_ticket_v3.py

I am also adding pydantic validators from week 11 in this project
for custom error as we are using router, the error will be placed inside the main file where fastapi , app is there

This version also include week 12 sql ai logging, so we will call ai log function from p07
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from P06_SmartOps_FastAPI.supabase_client import get_supabase_client
from P05_SmartOps_AI_Operations import classify_ticket_v2

from P07_SQL.AI_Log import SessionDep
from P07_SQL.AI_Log import log_ai_call
from P07_SQL.AI_Log import AILogCreate

import time

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

def calculate_cost(input_tokens : int, output_tokens :  int) -> float:
    input_cost = (input_tokens / 1000000) * 3.00
    output_cost = (output_tokens / 1000000) * 15.00

    return input_cost + output_cost
    
@router.post("/api/v1/classify_ticket")
def classify_ticket_endpoint(request : ClassifyTicketRequest, session: SessionDep):
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

    start_time = time.perf_counter()
    result, classify_metrics, reply_metrics = classify_ticket_v2.classify_ticket_v2(complaint_text)
    end_time = time.perf_counter()

    latency_ms = (end_time - start_time) * 1000

    """
    calling AI logging function to keep the logs checked
    """
    total_input_tokens = (classify_metrics.input_tokens + reply_metrics.input_tokens)
    total_output_tokens = (classify_metrics.output_tokens + reply_metrics.output_tokens)

    total_tokens = (classify_metrics.total_tokens + reply_metrics.total_tokens)
    total_cost_usd = calculate_cost(total_input_tokens, total_output_tokens)

    log_data = AILogCreate(
        endpoint = "/api/v1/classify_ticket",
        agency_id = request.agency_id,
        input_preview = complaint_text[:200],
        output_json = result.model_dump_json(),
        model_used = classify_metrics.model_used,
        cost_usd = total_cost_usd,
        token_used = total_tokens,
        latency_ms = latency_ms
    )

    log_ai_call(
        session = session,
        log_data=log_data
    )

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