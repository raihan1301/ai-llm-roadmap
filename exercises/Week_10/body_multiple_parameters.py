from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

"""
Body Model
"""
class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id : Annotated[int , Path(title = "Id of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item : Item | None = None
):
    results = {
        "item_id" : item_id
    }

    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" : item})

    return results
"""
Notice that, in this case, the item that would be taken from the body is optional. As it has a None default value.
"""
"""
request body :
item_id = 123
q = alpha
{
  "name": "foo",
  "description": "yo yo",
  "price": 30,
  "tax": 10
}

response body :
{
  "item_id": 123,
  "q": "alpha",
  "item": {
    "name": "foo",
    "description": "yo yo",
    "price": 30,
    "tax": 10
  }
}
"""

"""
below is the example of multiple body parameters
"""
class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {
        "item_id": item_id, 
        "item": item, 
        "user": user
    }
    return results
"""
Parameter :
item_id = 123
request body :
{
  "item": {
    "name": "Foo",
    "description": "item class",
    "price": 30,
    "tax": 10
  },
  "user": {
    "username": "romeo",
    "full_name": "rocky singh"
  }
}

Response body :
{
  "item_id": 123,
  "item": {
    "name": "Foo",
    "description": "item class",
    "price": 30,
    "tax": 10
  },
  "user": {
    "username": "romeo",
    "full_name": "rocky singh"
  }
}
"""

"""
below is the example of adding singular value into the response body but not as query parameter
we can import Body from fastapi and use the annotated keyword with body keyword
"""
from fastapi import Body

@app.put("/items3/{item_id}")
async def update_item( item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)] , q: str | None = None):
    results = {
        "item_id": item_id, 
        "item": item, 
        "user": user, 
        "importance": importance
    }

    if q:
        results.update({"q" : q})
    return results
"""
Path Parameter : item_id = 123
Query Parameter : q = alpha 

Request Body:
{
  "item": {
    "name": "foo",
    "description": "yo yo",
    "price": 30,
    "tax": 10
  },
  "user": {
    "username": "romeo",
    "full_name": "rocky sing"
  },
  "importance": 10
}

Response Body :
{
  "item_id": 123,
  "item": {
    "name": "foo",
    "description": "yo yo",
    "price": 30,
    "tax": 10
  },
  "user": {
    "username": "romeo",
    "full_name": "rocky sing"
  },
  "importance": 10,
  "q": "alpha"
}
"""

"""
below example is of embed body parameter
Body(embed=True) changes the request body you send into FastAPI, not the response you return.
"""
@app.put("/items4/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {
        "item_id": item_id, 
        "item": item
    }
    return results
"""
Path Parameter : item_id = 133
Request body:
{
  "item": {
    "name": "foo",
    "description": "yo yo",
    "price": 30,
    "tax": 10
  }
}

Response Body :
{
  "item_id": 133,
  "item": {
    "name": "foo",
    "description": "yo yo",
    "price": 30,
    "tax": 10
  }
}

Notice how request body has a key , and other request body in above example did not had any key
"""

"""
Below is the example of Body - field from pydantic
Field(...) lets you add rules to a Pydantic field.
"""

from pydantic import Field

class Item2(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None

@app.put("/items5/{item_id}")
async def update_item(item_id: int, item: Annotated[Item2, Body(embed=True)]):
    results = {
        "item_id": item_id, 
        "item": item
    }
    return results