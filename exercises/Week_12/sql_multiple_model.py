"""
In SQLModel, any model class that has table=True is a table model.
And any model class that doesn't have table=True is a data model, these ones are actually just Pydantic models 

IMP : With SQLModel, we can use inheritance to avoid duplicating all the fields in all the cases.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

"""
Initialization , it almost remain same in every code
"""
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"
connect_args = {"check_same_thread":  False}
engine = create_engine(sqlite_url, connect_args = connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


"""
Base Class
First lets create a base class which is acessible to everyone
"""
class HeroBase(SQLModel):
    name : str = Field(index = True)
    age : int | None = Field(default = None, index = True)


"""
Table Model
This class has extra fields and this will be inherit from base class so it can also use name and age
Imp : table = true it means is a table model. and above base class is a data model
"""
class Hero(HeroBase, table = True):
    id : int | None = Field(default = None, primary_key = True)
    secret_name : str


"""
Public Model
Now this model will be returned to client via API, so it inherits from BaseModel so it will have name and age
but we redeclare the id : int as well so the response contains the id as well
"""
class HeroPublic(HeroBase):
    id : int


"""
Hero Create :
this data model is to create Hero : this one will validate the data from clients
it will have seceret name, so when client send a new hero it will send secret name, but they will not get it in response, 
    it will be stored as secret
"""
class HeroCreate(HeroBase):
    secret_name : str


"""
Hero Update
this data model update the exisiting hero, all the fields is optional, so we only send field which we want to update
now fields actually change and can have None value, we have to re declare them
We don't really need to inherit from HeroBase because we are re-declaring all the fields. but for consistency i will inherit from Base class
"""
class HeroUpdate(HeroBase):
    name : str | None = None
    age : int | None = None
    secret_name : str | None = None


"""
Create with HeroCreate and return a HeroPublic
Now we create the Hero with Herocreate, which has base class fields as well and we return with HeroPublic class so we do not send secret_name
"""
@app.post("/heroes/", response_model = HeroPublic)
def create_hero(hero : HeroCreate, session : SessionDep):
    """
    hero is already a HeroCreate object.
    When client sends it will convert into HeroCreate, but HeroCreate is not our database table model, 
    so we need Hero object before inserting it into the Hero table, because Hero has table = true
    """
    db_hero = Hero.model_validate(hero)
    """
    The class before .model_validate() is the type of object I want to CREATE.
    db_hero = Hero.model_validate(hero) means Take the data from hero, validate it according to the Hero model, and create a new Hero object.
    HeroCreate → Hero
    """

    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)

    return db_hero
"""
TIP : 
Now we use response_model=HeroPublic instead of the return type annotation -> HeroPublic 
    because the value that we are returning is actually not a HeroPublic.
If we had declared -> HeroPublic, your editor and linter would complain (rightfully so) that you are returning a Hero instead of a HeroPublic.
By declaring it in response_model we are telling FastAPI to do its thing, without interfering with the type annotations 
    and the help from your editor and other tools.
"""


"""
Read Heroes with HeroPublic
we can do the same read and response model can be list of heropublic
"""
@app.get("/heroes/", response_model = list[HeroPublic])
def read_heroes(session : SessionDep, offset : int = 0, limit : Annotated[int, Query(le = 100)] = 100):
    heroes = session.exec(
        select(Hero)
        .offset(offset)
        .limit(limit)
    ).all()

    return heroes


"""
Read One Hero with HeroPublic
"""
@app.get("/heroes/{hero_id}", response_model = HeroPublic)
def read_hero(hero_id : int, session : SessionDep):
    hero = session.get(Hero, hero_id)

    if not hero:
        raise HTTPException(
            status_code = 404,
            detail = "Hero Not Found"
        )
    return hero


"""
Update a Hero with HeroUpdate
we use an HTTP PATCH operation. 
we get a dict with all the data sent by the client, but we only send data which needs to be updated, we use exclude_unset=True
"""
@app.patch("/heroes/{hero_id}", response_model = HeroPublic)
def update_hero(hero_id : int, hero : HeroUpdate, session : SessionDep):
    hero_db = session.get(Hero, hero_id)

    if not hero_db:
        raise HTTPException(
            status_code = 404,
            detail = "Hero Not Found"
        )

    hero_data = hero.model_dump(exclude_unset = True)
    """
    we are dumping all the info send by client inside hero_data but excluding any none values
    """
    hero_db.sqlmodel_update(hero_data)

    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)

    return hero_db


"""
Delete a Hero Again
Deleting a hero stays pretty much the same.
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
        "Ok" : True
    }