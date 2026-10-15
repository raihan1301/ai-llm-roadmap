from P07_SQL.AI_Log import (AILog, SessionDep)

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, field_validator

from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import func
from datetime import datetime, timezone

router = APIRouter()

"""
output class
"""
class AIStatsPublic(BaseModel):
    calls_today : int
    avg_latency_ms : float
    total_cost_usd : float
    top_endpoint : str | None


@router.get("/api/v1/stats")
def get_stats(session: SessionDep, response_model = AIStatsPublic):
    """
    Here we will add all the necessary stats needed to client
    """

    """
    SQLite is storing our UTC datetime without the timezone part,
    so we create today's UTC starting point and remove tzinfo.
    """
    start_of_today = (
        datetime.now(timezone.utc)
        .replace(
            hour = 0,
            minute = 0,
            second = 0,
            microsecond = 0
        )
        .replace(tzinfo = None)
    )

    """
    First lets take AI calls made today
    """
    calls_today = session.exec(
        select(func.count(AILog.id))
        .where(AILog.created_at >= start_of_today)
    ).one()
    """
    means: count the number of AILog records whose created_at is today or later. 
    func.count() is basically SQL's COUNT() function. If you made 7 AI calls today, this returns 7.
    .one() means: give me exactly one result from this query.
    """


    """
    Now we get latency across all logged calls today
    """
    avg_latency_ms = session.exec(
        select(func.avg(AILog.latency_ms))
        .where(AILog.created_at >= start_of_today)
    ).one()
    """
    means: take every latency_ms value and calculate the average. With values like:
    """


    """
    Now total AI cost across all log today
    """
    total_cost_usd = session.exec(
        select(func.sum(AILog.cost_usd))
        .where(AILog.created_at >= start_of_today)
    ).one()
    """
    does the same idea for cost. sum of all the cost
    """


    """
    Endpoint that has been called most
    """
    top_endpoint_result = session.exec(
        select(
            AILog.endpoint, func.count(AILog.id).label("call_count")
        )
        .group_by(AILog.endpoint)
        .order_by(func.count(AILog.id).desc())
        .limit(1)
    ).first()
    """
    we can also write :

    call_count = func.count(AILog.id).label("call_count")

    top_endpoint_result = session.exec(
        select(
            AILog.endpoint,
            call_count
        )
        .group_by(AILog.endpoint)
        .order_by(call_count.desc())
        .limit(1)
    ).first()
    """
    if top_endpoint_result:
        top_endpoint = top_endpoint_result[0]
    else:
        top_endpoint = None
    """
    .group_by(AILog.endpoint) :groups identical endpoints together
    .order_by(func.count(AILog.id).desc()) : sorts from highest count to lowest:
    .first() means: give me the first row from the result, or None if there are no rows.
    We already calculated the count in select(), so in SQL you can often order by that alias, conceptually: ORDER BY call_count DESC
        But in SQLAlchemy/SQLModel, reusing the exact count expression is often the simplest and clearest: 
            .order_by(func.count(AILog.id).desc()) : the count is now calculated inside each endpoint group. and not individually
    """

    return AIStatsPublic(
        calls_today=int(calls_today or 0),
        avg_latency_ms=round(float(avg_latency_ms or 0), 2),
        total_cost_usd=round(float(total_cost_usd or 0), 6),
        top_endpoint=top_endpoint
    )
"""
The or 0 pieces here: are important because if your database is completely empty, SQL's AVG() and SUM() can return None. 
    We don't want your API response to become: "avg_latency_ms": null so we convert an empty result to 0.
avg_latency_ms=round(float(avg_latency_ms or 0), 2), : here 2 means round the number to 2 digits after the decimal point.
"""


