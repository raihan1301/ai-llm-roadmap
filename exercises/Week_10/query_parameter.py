from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name" : "foo"},
    {"item_name" : "bar"},
    {"item_name" : "baz"}
]
"""
IMP : if the parameters are not in path, 
function parameters will be treated as query parameters

but if function parameter is passed inside the path using {} that that is path parameter
"""
"""
IMP : 
GET means the client is asking the server for data.
client might call :/items_4/123?needy=yes&skip=0&limit=10
sends the result back to the client.
"""
@app.get("/items/")
async def read_item(skip : int = 0, limit : int = 10):
    """
    Two parameter skip and limit
    """
    return fake_items_db[skip : skip + limit]
    """
    if skip is 0 and limit is 2
    fake_items_db[0 : 0 + 2] so all the items from index 0 to 2
    """

"""
Results
http://127.0.0.1:8000/items  : [{"item_name":"foo"},{"item_name":"bar"},{"item_name":"baz"}]
http://127.0.0.1:8000/items/?skip=0&limit=10 : [{"item_name":"foo"},{"item_name":"bar"},{"item_name":"baz"}]
http://127.0.0.1:8000/items/?skip=1&limit=10 : [{"item_name":"bar"},{"item_name":"baz"}]
http://127.0.0.1:8000/items/?skip=0&limit=2 : [{"item_name":"foo"},{"item_name":"bar"}]
"""

"""
below is the example of optional query parameter
"""
@app.get("/items/{item_id}")
async def read_item(item_id : str, q :str | None = None):
    if q:
        return {"item_id" : item_id, "q" : q}
    return {"item_id" : item_id}

"""
http://127.0.0.1:8000/items/foo?q=lob : {"item_id":"foo","q":"lob"}
http://127.0.0.1:8000/items/foo : {"item_id":"foo"}
"""

"""
below is the example of query parameter conversion, with bool
"""
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id" : item_id}

    if q:
        item.update({"query" : q})

    if not short:
        item.update({"description" : "This is amazing"})

    return item
"""
http://127.0.0.1:8000/items2/foo?q=yes : {"item_id":"foo","query":"yes","description":"This is amazing"}
http://127.0.0.1:8000/items2/foo : {"item_id":"foo","description":"This is amazing"}
http://127.0.0.1:8000/items2/foo?q=yes&short=true : {"item_id":"foo","query":"yes"}
"""

"""
Below example is of multiple path and query parameter
"""
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

"""
http://127.0.0.1:8000/users/123/items/foo : {"item_id":"foo","owner_id":123,"description":"This is an amazing item"}
http://127.0.0.1:8000/users/123/items/foo?q=yes : {"item_id":"foo","owner_id":123,"q":"yes","description":"This is an amazing item"}
http://127.0.0.1:8000/users/123/items/foo?q=yes&short=true : {"item_id":"foo","owner_id":123,"q":"yes"}
"""

"""
below example is for required parameter
"""
@app.get("/items_3/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

"""
http://127.0.0.1:8000/items_3/foo : {"detail":[{"type":"missing","loc":["query","needy"],"msg":"Field required","input":null}]}
http://127.0.0.1:8000/items_3/foo?needy=no : {"item_id":"foo","needy":"no"}
"""

"""
Recap :some parameters as required, some as having a default value, and some entirely optional:
"""
@app.get("/items_4/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

"""
needy, a required str.
skip, an int with a default value of 0.
limit, an optional int.
"""