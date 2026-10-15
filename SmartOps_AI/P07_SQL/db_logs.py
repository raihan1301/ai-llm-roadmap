from P07_SQL.AI_Log import (AILog, SessionDep)

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, field_validator

from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime, timezone

router = APIRouter()

"""
Output BaseModel because we need to hide some fields for security
"""
class AILogPublic(SQLModel):
    id: int
    endpoint: str
    model_used: str
    token_used: int
    latency_ms: float
    created_at: datetime

@router.get("/api/v1/logs", response_model= list[AILogPublic])
def get_logs(session : SessionDep, skip : int = 0, limit : int = Query(default=20, le=100)):
    logs = session.exec(
        select(AILog)
        .order_by(AILog.created_at.desc())
        .offset(skip)
        .limit(limit)
    ).all()

    return logs

"""
[
  {
    "id": 1,
    "endpoint": "/api/v1/classify_ticket",
    "model_used": "claude-sonnet-4-6",
    "token_used": 2297,
    "latency_ms": 10035.894100088626,
    "created_at": "2026-10-12T02:15:22.603721Z"
  }
]
"""

"""
pagination is :
skip: int = 0
limit: int = Query(default=20, le=100)
.offset(skip)
.limit(limit)
"""