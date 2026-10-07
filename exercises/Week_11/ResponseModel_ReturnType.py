from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    item.price = 50.0
    item.tax = 10
    return item
"""
Request body came from client : 
{
    "name": "Apple",
    "description": "Fruit price",
    "price" : 0
}

Response Body given send to client : 
{
  "name": "Apple",
  "description": "Fruit price",
  "price": 50,
  "tax": 10,
  "tags": []
}
"""


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0, tax=5.0),
    ]
"""
URL : http://127.0.0.1:8000/items/
return response : 
[
  {
    "name": "Portal Gun",
    "description": null,
    "price": 42,
    "tax": null,
    "tags": []
  },
  {
    "name": "Plumbus",
    "description": null,
    "price": 32,
    "tax": 5,
    "tags": []
  }
]
"""

"""
Response model parameter example
"""
from typing import Any

@app.post("/items2/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items2/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

"""
response_model receives the same type you would declare for a Pydantic model field, so, it can be a Pydantic model, 
but it can also be, e.g. a list of Pydantic models, like List[Item].
"""

"""
In below example you will see same input data and return the same data
"""
from pydantic import EmailStr

class UserIn(BaseModel):
    username : str
    password : str
    email : EmailStr
    full_name : str | None = None

@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user
"""
Request Body:
{
  "username": "raihan1301",
  "password": "kapadia@1234",
  "emai": "raihan@gmail.com",
  "full_name": "string"
}
Response Body : 
{
  "username": "raihan1301",
  "password": "kapadia@1234",
  "emai": "raihan@gmail.com",
  "full_name": "string"
}

IMP : Never store the plain password of a user or send it in a response like this, unless you know all the caveats and you know what you are doing.
"""

"""
Below example is different pydantic input model and different output model
we will use UserIn input model from above
"""
class UserOut(BaseModel):
    username : str
    email : EmailStr
    full_name : str | None = None

@app.post("/user2/", response_model = UserOut)
async def create_user(user : UserIn) -> Any:
    return user
"""
Request Body : 
{
  "username": "raihan1301",
  "password": "Kapadia@123",
  "email": "raihan@gmail.com",
  "full_name": "Raihan Kapadia"
}

Response Body : 
{
  "username": "raihan1301",
  "email": "raihan@gmail.com",
  "full_name": "Raihan Kapadia"
}
IMP body request and response should have same key name
we declared the response_model to be our model UserOut, that doesn't include the password:
"""

"""
Below example is of return type using classes and inheritance, so model can support
"""
class BaseUser(BaseModel):
    username : str
    email : EmailStr
    full_name : str | None = None

class UserIn2(BaseUser):
    password : str

@app.post("/user3/")
async def create_user(user : UserIn2) -> BaseUser:
    return user
"""
Same output like above example
"""

"""
Other return type annotations : return a response directly
"""
from fastapi import Response
from fastapi.responses import JSONResponse, RedirectResponse

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})
"""
This simple case is handled automatically by FastAPI because the return type annotation is the class (or a subclass of) Response.
"""
"""
URL : http://127.0.0.1:8000/portal
{
  "message": "Here's your interdimensional portal."
}

URL : http://127.0.0.1:8000/portal?teleport=true
It will redirect to "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
"""

"""
We can use the annotated response subclass direct as well
"""
@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

"""
Invalid return type example that will fail , i have to put it in comments other wise i cant run the file for other code
"""
"""
@app.get("/portal2")
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}
"""
"""
this fails because the type annotation is not a Pydantic type and is not just a single Response class or subclass, 
    it's a union (any of the two) between a Response and a dict.
"""

"""
Below example is to correct above wrong code by disable the repsonse model
"""
@app.get("/portal2", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}
"""
This will make FastAPI skip the response model generation and 
    that way you can have any return type annotations you need without it affecting your FastAPI application.
"""

"""
Now let say BaseModel contain some default values, but we want to exclude them and include only when they are actually set
below is that example
"""
class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items2 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items2/{item_id}", response_model=Item2, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items2[item_id]
"""
URL : http://127.0.0.1:8000/items2/foo
{
  "name": "Foo",
  "price": 50.2
}

If we did not had "response_model_exclude_unset=True" we would have got the default values as well
{
  "name": "Foo",
  "description": null,
  "price": 50.2,
  "tax": 10.5,
  "tags": []
}

but remember if you have the actual value for that default value, it will get return
URL : http://127.0.0.1:8000/items2/bar
{
  "name": "Bar",
  "description": "The bartenders",
  "price": 62,
  "tax": 20.2
}

Note :Data with the same values as the defaults : so if the actual value is same as default value, still does not matter, 
    fastapi is smart enough to include them
"""

"""
Below example is of include the model values inside the json or exclude it,
"""
@app.get(
    "/items3/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items2[item_id]


@app.get("/items3/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items2[item_id]

"""
URL : http://127.0.0.1:8000/items3/foo/name
{
  "name": "Foo",
  "description": null
}
Here you can see description is included, but price is not included evn though there is a price value
because of response_model_include={"name", "description"}

URL : http://127.0.0.1:8000/items3/foo/public
{
  "name": "Foo",
  "description": null,
  "price": 50.2,
  "tags": []
}
Here you can see only tax is removed because response_model_exclude={"tax"}

Note : if you pass list instead of set, no worries fastapi will convert into set or dict as needed
for example : response_model_include={"name", "description"}  this and response_model_include=["name", "description"] will be same
"""