from fastapi import FastAPI

app = FastAPI()

@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
"""
Here you can see we passed the status code 201 which is for create

Request URL : http://127.0.0.1:8000/items/?name=arhan
code : 201
{
  "name": "arhan"
}
"""

"""
Now if you do not want to remember which code does what use convenenice status from fastapi.status
"""

from fastapi import status

@app.post("/items2/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}