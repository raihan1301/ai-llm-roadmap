from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
"""
IMP:
POST usually means the client sends data to the server.
client send :
{
  "name": "Laptop",
  "price": 1200
}

whatever you return from create_item() is the response sent back to the client.
"""
"""
below is creating a data model
"""
class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None

"""
declare this class as parameter in below function
"""
@app.post("/items/")
async def create_item(item : Item):
    """
    use the model inside this function
    """
    item_dict = item.model_dump()

    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

"""
request body:
{
  "name": "string",
  "description": "string",
  "price": 50,
  "tax": 13
}

Output response body:
{
  "name": "string",
  "description": "string",
  "price": 50,
  "tax": 13,
  "price_with_tax": 63
}
"""

"""
below example is of request body + path parameter
"""
@app.put("/items/{item_id}")
async def update_item(item_id : int, item: Item):
    return {
        "item_id" : item_id,
        **item.model_dump()
    }

"""
in url item_id = 123  , ex url : http://127.0.0.1:8000/items/123
request body :
{
  "name": "string",
  "description": "string",
  "price": 25,
  "tax": 10
}

response body :
{
  "item_id": 123,
  "name": "string",
  "description": "string",
  "price": 25,
  "tax": 10
}
"""

"""
below is the example of request body + parth + query parameter
"""
@app.put("/items2/{item_id}")
async def update_item(item_id : int, item : Item, q : str | None = None):
    result = {
        "item_id" : item_id,
        **item.model_dump()
    }

    if q:
        result.update({"q" : q})
    return result

"""
URL : http://127.0.0.1:8000/items2/123?q=foo

Request Body :
{
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
}

Response Body:
{
  "item_id": 123,
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0,
  "q": "foo"
}
"""