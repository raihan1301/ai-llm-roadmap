from fastapi import FastAPI

app = FastAPI() 


"""
parameter inside the path
"""
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id}

"""
The value of the path parameter item_id will be passed to your function as the argument item_id.
example :http://127.0.0.1:8000/items/foo
you will get {"item_id" : "foo"}
"""

"""
parameters with types
"""
@app.get("/items_2/{item_id}")
async def read_item(item_id: int):
    return {"item_id" : item_id}


"""
parameters order matters, when there is a mixed path see below example
otherwise it will select the first matching path

Similarly, you cannot redefine a path operation: because it will always select the first so you cannot use same path twice
"""
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}