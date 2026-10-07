from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    """
    This model_config forbid any extra query send by client
    If a client tries to send some extra data in the query parameters, they will receive an error response.
    """

    limit : int = Field(100, gt=0, le=100)
    """
    Field(...) lets you add rules to a Pydantic field.
    limit must be an integer, default value = 100, must be greater than 0, must be less than or equal to 100
    """
    offset : int = Field(0,ge=0)
    order_by : Literal["created_at", "updated_at"] = "created_at"
    """
    Literal means only these two string values are allowed: default value is "created_at"
    """
    tags: list[str] = []
    """
    tags is a list of strings. The client could send something like: ?tags=python&tags=fastapi
    """

@app.get("/items/")
async def read_items(filter_query : Annotated[FilterParams, Query()]):
    return filter_query


"""
FastAPI will extract the data for each field from the query parameters in the request and give you the Pydantic model you defined.
"""
"""
URL : http://127.0.0.1:8000/items/?limit=10&tool=plumbus
{
  "detail": [
    {
      "type": "extra_forbidden",
      "loc": [
        "query",
        "tool"
      ],
      "msg": "Extra inputs are not permitted",
      "input": "plumbus"
    }
  ]
}
"""

"""
URL : http://127.0.0.1:8000/items/?limit=25&offset=50&order_by=updated_at&tags=python&tags=fastapi
{
  "limit": 25,
  "offset": 50,
  "order_by": "updated_at",
  "tags": [
    "python",
    "fastapi"
  ]
}
"""