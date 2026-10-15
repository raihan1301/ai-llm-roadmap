"""
The main reason for this main.py is to make one FastAPI Application and add router for other files
"""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from P06_SmartOps_FastAPI.classify_ticket_v3 import router as classify_router
from P06_SmartOps_FastAPI.health import router as health_router
from P06_SmartOps_FastAPI.summarize_complaint_v2 import router as summary_router
from P06_SmartOps_FastAPI.extract_contract_v2 import router as contract_router
from P06_SmartOps_FastAPI.draft_followup_v2 import router as draft_router

from P07_SQL.db_logs import router as log_router
from P07_SQL.db_stats import router as stats_router
from P07_SQL.contract_scorer import router as contract_scorer_router

"""
app = FastAPI()
we can just use the above code to start an fast api app.
but we are also doing logging into AI log database and we need to create a session so we have to use contextmanager
"""
from P07_SQL.AI_Log import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request : Request, exc : RequestValidationError):
    
    errors = []

    for error in exc.errors():
        errors.append({
            "field" : error["loc"][-1],
            "error" : error["type"],
            "message" : error["msg"]
        })

    return JSONResponse(
        status_code = 422,
        content = {
            "errors" : errors
        }
    )

"""
If any unexpected Python exception happens and no more specific handler catches it, send it here."
The client sees only: internal_error
but your server terminal can still show: Unexpected Error : {repr(exc)}
"""
@app.exception_handler(Exception)
def global_exception_handler(request : Request, exc : Exception):
    print(f"Unexpected Error : {repr(exc)}")
    return JSONResponse(
        status_code = 500,
        content = {
            "error" : "internal_error"
        }
    )

app.include_router(health_router)
app.include_router(classify_router)
app.include_router(summary_router)
app.include_router(contract_router)
app.include_router(draft_router)
app.include_router(log_router)
app.include_router(stats_router)
app.include_router(contract_scorer_router)