from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id : Annotated[int, Path(title = "Id of Item")], q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {
        "item_id" : item_id
    }

    if q:
        results.update({"q" : q})
    return results

"""
Note : You can declare all the same parameters as for Query.
"""

"""
Below example of order the parameters without Annotated
"""
@app.get("/items2/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    """
    If you do not use annotated and what to put non default value at last you can use *
    async def read_items( *, item_id: int = Path(title="The ID of the item to get"), q: str )
    """
    results = {
        "item_id" : item_id
    }

    if q:
        results.update({"q" : q})
    return results  
"""
TIP :It doesn't matter for FastAPI. It will detect the parameters by their names, types and default declarations (Query, Path, etc), 
it doesn't care about the order.
Note : Python will complain if you put a value with a "default" before a value that doesn't have a "default".
"""  

"""
Below example of order the parameters with Annotated
"""
@app.get("/items3/{item_id}")
async def read_items(q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]):
    """
    with annotated you can write like this as well 
    async def read_items( item_id: Annotated[int, Path(title="The ID of the item to get")], q: str )
    """
    results = {
        "item_id" : item_id
    }

    if q:
        results.update({"q" : q})
    return results 


"""
Number validations: greater than or equal
Here, with ge=1, item_id will need to be an integer number "greater than or equal" to 1.
"""
@app.get("/items4/{item_id}")
async def read_items( item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str ):
    """
    for greater than - gt or less than or equal - le, below is the function
    async def read_items( item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)], q: str,):
    """
    results = {
        "item_id" : item_id
    }

    if q:
        results.update({"q" : q})
    return results
"""
URL : http://127.0.0.1:8000/items4/0?q=alpha
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be greater than or equal to 1",
      "input": "0",
      "ctx": {
        "ge": 1
      }
    }
  ]
}
"""

"""
Below example is of number validation
"""
@app.get("/items/{item_id}")
async def read_items(*, 
                    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)], 
                    q: str, 
                    size: Annotated[float, Query(gt=0, lt=10.5)],):
    results = {
        "item_id" : item_id
    }
    if q:
        results.update({"q" : q})
    if size:
        results.update({"size": size})
    return results