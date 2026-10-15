"""
This will log every AI request we did with the models
"""
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

from datetime import datetime, timezone
from contextlib import asynccontextmanager

"""
Initialization
"""
sqlite_filename = "AiLog.db"
sqlite_url = f"sqlite:///{sqlite_filename}"
connect_args = {"check_same_thread":  False}
engine = create_engine(sqlite_url, connect_args = connect_args)

"""
Create the tables : this is to create the tables for all the table models.
If table exist it does nothing
"""
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

"""
Create a session
"""
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


"""
on event is getting deprecated so use lifespan

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
"""

"""
we do not need this because we have initalize in p06 main.py

@asynccontextmanager
async def lifespan(app : FastAPI):
    create_db_and_tables()
    yield
"""

"""
Create Database Tables on Startup 
we do not need this because we have initalize in p06 main.py

app = FastAPI(lifespan=lifespan)
"""

"""
AI Log Model
"""
class AILog(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key=True)
    endpoint : str

    agency_id : str

    input_preview : str
    output_json : str

    model_used : str

    cost_usd : float
    token_used : int
    latency_ms : float

    created_at : datetime = Field(default_factory= lambda: datetime.now(timezone.utc))


"""
Now we create a generic logging function so all the files can call it 
this function will than use above class
"""
"""
def log_ai_call(session : SessionDep, log_data : AILog):
we can write like this as well but we created AILogCreate is not because AILog(table=True) cannot be used. 
    It is mainly for cleaner separation.

AILog has your actual database table and also contains database-managed fields such as: id, created_at, which is not needed as input
"""
class AILogCreate(SQLModel):
    endpoint : str
    agency_id : str
    
    input_preview : str
    output_json : str
    
    model_used : str
    
    cost_usd : float
    token_used : int
    latency_ms : float

def log_ai_call(session : Session, log_data : AILogCreate):
    log = AILog.model_validate(log_data)
    """
    we validate our input data with the actual database model
    """

    session.add(log)
    session.commit()
    session.refresh(log)