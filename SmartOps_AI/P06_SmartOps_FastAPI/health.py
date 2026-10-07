"""
Purpose of this health.py is that our server is live or not
we can set up a rotuine call every hour and get a status ok,
if status is not ok , we can set up an alert which can tell us our server is down
"""
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/health")
def health():
    return{
        "status" : "ok",
        "version" : "1.0"
    }