"""
We'll create the simplest first version of the app with a single SQLModel model first.
Later we'll improve it increasing security and versatility with multiple models below.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


"""
This below code is creating a model
"""
class Hero(SQLModel, table = True):
    id : int | None = Field(default=None, primary_key = True)
    name : str = Field(index = True)
    age : int | None = Field(default = None, index = True)
    secret_name : str
    """
    Field() doesn't only mean validation; it also lets you configure how that field behaves in the database
    """


"""
Create an engine : hold connection to database
Using check_same_thread=False allows FastAPI to use the same SQLite database in different threads
"""
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

connect_args = {"check_same_thread":  False}
engine = create_engine(sqlite_url, connect_args = connect_args)
"""
It's perfectly normal to look up the exact create_engine() syntax when building a project.
sqlite_filename = "database.db" is the actual file SQLite will create on your computer.
sqlite_url = "sqlite:///database.db" is the connection string SQLAlchemy/SQLModel understands
"""


"""
Create the tables : this is to create the tables for all the table models.
"""
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
"""
SQLModel.metadata knows about all the classes you've declared with table=True, such as Hero, and create_all(engine) tells the database:
Look at all my SQLModel table models -> Check this database -> Create any tables that don't already exist
"""


"""
Create a Session Dependency
Session stores the objects in memory and changes and than use engine to communicate with database
We use FastAPI dependency with yield that will provide new session for each request
"""
def get_session():
    with Session(engine) as session:
        yield session
        """
        A Session is basically your working conversation with the database.
        Think of the engine as the main database connection/configuration object. SQLModel uses it to know which database it should talk to. 
        when you create a Session(engine), you're basically saying: "Give me a working database session using this database."
        """
        """
        opens a session, gives it temporarily to the FastAPI endpoint, and once that request finishes, the with block closes the session properly.
        """

SessionDep = Annotated[Session, Depends(get_session)]
"""
You're creating a reusable type that tells FastAPI: 
    Whenever an endpoint asks for SessionDep, call get_session() and give that endpoint the database session.
"""


"""
Create Database Tables on Startup : We will create the database tables when the application starts.
Note :Here we create the tables on an application startup event. 
    For production you would probably use a migration script that runs before you start your app
"""
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    """
    FastAPI starts, it calls: create_db_and_tables(), which checks whether the SQLModel tables exist and creates the missing ones.
    But importantly, it does not delete your previous data. Suppose yesterday your database had:
    """


"""
Create a Hero : 
SQLModel is pydantic model so we can use it same like it will read from json body and can be use in return type

Explanation : Here we use the SessionDep dependency (a Session) to add the new Hero to the Session instance, 
    commit the changes to the database, refresh the data in the hero, and then return it.
"""
@app.post("/heroes/")
def create_hero(hero : Hero, session : SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero
"""
session.refresh(hero) : reloads the object so Python now has: the id as well i mean whole sql model for that particular object
"""


"""
Read Heroes :
We can read Heros from the database using a select(). We can include a limit and offset to paginate the results.
"""
@app.get("/heroes/")
def read_heroes(session : SessionDep, offset : int = 0, limit : Annotated[int, Query(le=100)] = 100,) -> list[Hero]:
    heroes = session.exec(
        select(Hero)
        .offset(offset)
        .limit(limit)
    ).all()

    return heroes
""" Behind Scene
Request comes in
      ↓
FastAPI sees SessionDep
      ↓
calls get_session()
      ↓
creates Session(engine)
      ↓
gives session to endpoint
      ↓
endpoint finishes
      ↓
session closes
"""


"""
Read One Hero
"""
@app.get("/heroes/{hero_id}")
def read_hero(hero_id : int, session : SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)

    if not hero:
        raise HTTPException(
            status_code = 404,
            detail = "Hero Not Found"
        )

    return hero


"""
delete a hero
"""
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id : int, session : SessionDep):
    hero = session.get(Hero, hero_id)

    if not hero:
        raise HTTPException(
            status_code = 404,
            detail = "Hero Not Found"
        )

    session.delete(hero)
    session.commit()
    return {
        "ok" : True
    }

"""
Some results:

created two records
{
    "name": "almas",
    "age": 30,
    "secret_name": "allu",
    "id": 0
}
{
    "name": "raihan",
    "age": 32,
    "secret_name": "railu"
}

get
[
  {
    "name": "almas",
    "age": 30,
    "secret_name": "allu",
    "id": 0
  },
  {
    "name": "raihan",
    "age": 32,
    "secret_name": "railu",
    "id": 1
  }
]

single hero with id : 1
{
  "name": "raihan",
  "age": 32,
  "secret_name": "railu",
  "id": 1
}

deleted id : 0
{
  "ok": true
}
"""