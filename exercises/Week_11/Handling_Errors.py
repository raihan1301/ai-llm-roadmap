from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={"X-Error": "There goes my error"},)
    return {
        "item": items[item_id]
    }
"""
URL : http://127.0.0.1:8000/items/foo
{
  "item": "The Foo Wrestlers"
}

URL : http://127.0.0.1:8000/items/bar
{
  "detail": "Item not found"
}
Above example also trach us to add custom headers inside the exception
"""

"""
Below is the example of custom exception handler
"""
from fastapi import Request
from fastapi.responses import JSONResponse

class UnicornException(Exception):
    def __init__(self, name : str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request : Request, exc: UnicornException):
    return JSONResponse(
        status_code = 418,
        content = {"message" : f"Oops ! {exc.name} did something. there goes a rainbow...."}
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name : str):
    if name == "yolo":
        raise UnicornException(name = name)
    return {"unicorn_name" : name}
"""
Here, if you request /unicorns/yolo, the path operation will raise a UnicornException.
But it will be handled by the unicorn_exception_handler.
So, you will receive a clean error, with an HTTP status code of 418 and a JSON content of: {"message": "Oops! yolo did something. There goes a rainbow..."}
"""

"""
Override the default exception handlers
"""
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

"""
below method is Override the HTTPException error handler
you could want to return a plain text response instead of JSON for these errors:
"""
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code = exc.status_code)

"""
This below method is to override request validation exceptions
"""
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc : RequestValidationError):
    message = "validation errors"
    for error in exc.error():
        message += f"\n Field: {error['loc']}, Error: {error['msg']}"
    return PlainTextResponse(message, status_code = 400)

@app.get("/items/{item_id}")
async def read_items(item_id : int):
    if item_id == 3:
        raise HTTPException(status_code = 418, detail="Nope ! i dont like 3.")
    return {"item_id" : item_id}
"""
Now, if you go to /items/foo, instead of getting the default JSON error with:
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}

you will get a text version, with:
Validation errors:
Field: ('path', 'item_id'), Error: Input should be a valid integer, unable to parse string as an integer
"""

"""
Example for request validation error body
"""
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item

"""
Now try sending an invalid item like:
{
  "title": "towel",
  "size": "XL"
}

You will receive a response telling you that the data is invalid containing the received body:
{
  "detail": [
    {
      "loc": [
        "body",
        "size"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ],
  "body": {
    "title": "towel",
    "size": "XL"
  }
}
"""

"""
reusing the same FastAPI exception handler
"""
from fastapi.exception_handlers import (http_exception_handler,request_validation_exception_handler,)

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)

@app.get("/items5/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}

"""
URL : http://127.0.0.1:8000/items5/alpha  : this is invalid item_id
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "alpha"
    }
  ]
}
OMG! The client sent invalid data!: 1 validation error:

URL : http://127.0.0.1:8000/items5/3 : raise HTTPException
{
  "detail": "Nope! I don't like 3."
}
OMG! An HTTP error!: HTTPException(status_code=418, detail="Nope! I don't like 3.")
"""

"""
GET /items5/3
      ↓
read_item()
      ↓
item_id == 3
      ↓
raise HTTPException(...)
      ↓
FastAPI looks for matching exception handler
      ↓
custom_http_exception_handler(request, exc)
      ↓
prints:
OMG! An HTTP error!
      ↓
calls FastAPI's built-in handler:
http_exception_handler(request, exc)
      ↓
returns the normal FastAPI error response
"""