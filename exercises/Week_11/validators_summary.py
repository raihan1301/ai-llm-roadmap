"""
This file gives example of both decorator and Annotated
"""
from typing import Any, Annotated
from pydantic import (BaseModel, ValidationError, field_validator, BeforeValidator, AfterValidator)
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()
"""
field validator - after mode
"""
class ComplaintRequest(BaseModel):
    complaint_text: str
    agency_id: str

    @field_validator("complaint_text", mode="after")
    @classmethod
    def validate_complaint_text(cls, value: str) -> str:
        value = value.strip()

        if len(value) < 10:
            raise ValueError(
                "complaint_text must be at least 10 characters"
            )

        return value

    @field_validator("agency_id", mode="after")
    @classmethod
    def validate_agency_id(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("agency_id cannot be empty")

        return value

"""
field validator - Before mode
"""
class DraftFollowupRequest(BaseModel):
    contract_id: str
    agency_id: str

    @field_validator("contract_id", "agency_id",mode="before")
    @classmethod
    def clean_and_validate(cls,value: Any) -> Any:

        # Before validator receives raw input.
        if isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError("field cannot be empty")

        return value

"""
Annotated Validations
"""
def clean_non_empty_string(value: Any) -> Any:
    """
    BEFORE validator: clean whitespace before Pydantic validates `str`.
    """
    if isinstance(value, str):
        value = value.strip()

        if not value:
            raise ValueError("field cannot be empty")
    return value

def contract_value_must_be_positive(value: float) -> float:
    """
    AFTER validator: Pydantic has already confirmed this is a float.
    """
    if value <= 0:
        raise ValueError("contract_value must be greater than 0")
    return value

NonEmptyString = Annotated[str,BeforeValidator(clean_non_empty_string)]
PositiveContractValue = Annotated[float,AfterValidator(contract_value_must_be_positive)]

class ContractRequest(BaseModel):
    contract_id: NonEmptyString
    agency_id: NonEmptyString
    contract_value: PositiveContractValue

"""
Test
"""
print("\n--- AFTER FIELD VALIDATOR ---")
try:
    complaint = ComplaintRequest(
        complaint_text="Guard arrived 30 minutes late",
        agency_id="   company-x   "
    )
    print(complaint)
except ValidationError as err:
    print(err)


print("\n--- BEFORE FIELD VALIDATOR ---")
try:
    followup = DraftFollowupRequest(
        contract_id="   contract-123   ",
        agency_id="   company-x   "
    )
    print(followup)
except ValidationError as err:
    print(err)


print("\n--- ANNOTATED VALIDATORS ---")
try:
    contract = ContractRequest(
        contract_id="   contract-123   ",
        agency_id="   company-x   ",
        contract_value=5000
    )
    print(contract)
except ValidationError as err:
    print(err)


print("\n--- INVALID COMPLAINT ---")
try:
    ComplaintRequest(
        complaint_text="bad",
        agency_id=""
    )
except ValidationError as err:
    print(err)


print("\n--- INVALID CONTRACT VALUE ---")
try:
    ContractRequest(
        contract_id="contract-123",
        agency_id="company-x",
        contract_value=-500
    )
except ValidationError as err:
    print(err)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,exc: RequestValidationError):
    error = exc.errors()[0]

    return JSONResponse(
        status_code=422,
        content={
            "field": error["loc"][-1],
            "error": error["type"],
            "message": error["msg"]
        }
    )
