from fastapi import FastAPI, Query
from typing import Annotated 

app = FastAPI()

@app.get("/items")
async def read_items(q: str | None = None):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }

    if q:
        results.update({"q" : q})
    return results

"""
URL : http://127.0.0.1:8000/items?q=tar

results:
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    }
  ],
  "q": "tar"
}

Note if we do this in above code :  results["items"].append({"item_id": q})
results :
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    },
    {
      "item_id": "tar"
    }
  ]
}
"""

@app.get("/items2/")
async def read_items(q: Annotated[str | None, Query(max_length=10)] = None):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
    
    if q:
        results.update({"q" : q})
    return results

"""
URL : http://127.0.0.1:8000/items2/?q=tarbferjkfhjekrgherghreklhreedhfek
{
  "detail": [
    {
      "type": "string_too_long",
      "loc": [
        "query",
        "q"
      ],
      "msg": "String should have at most 10 characters",
      "input": "tarbferjkfhjekrgherghreklhreedhfek",
      "ctx": {
        "max_length": 10
      }
    }
  ]
}
"""

"""
Some old version use query as default parameter, it is one of the same thing but keep in mind
"""
@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
        
    if q:
        results.update({"q" : q})
    return results


"""
Add a additional parameter
"""
@app.get("/items3/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
            
    if q:
        results.update({"q" : q})
    return results
"""
URL : http://127.0.0.1:8000/items3/?q=t
{
    "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "query",
        "q"
      ],
      "msg": "String should have at least 3 characters",
      "input": "t",
      "ctx": {
        "min_length": 3
      }
    }
  ]
}
"""

"""
Below is the example of having regular expression in annotated way
"""
@app.get("/items4/")
async def read_items(q : Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
                
    if q:
        results.update({"q" : q})
    return results
"""
URL : http://127.0.0.1:8000/items4/?q=tarzan
{
  "detail": [
    {
      "type": "string_pattern_mismatch",
      "loc": [
        "query",
        "q"
      ],
      "msg": "String should match pattern '^fixedquery$'",
      "input": "tarzan",
      "ctx": {
        "pattern": "^fixedquery$"
      }
    }
  ]
}
"""

"""
Below is the example of Default values
"""
@app.get("/items5/")
async def read_items(q : Annotated[str, Query(min_length= 3)] = "fixedquery"):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
                    
    if q:
        results.update({"q" : q})
    return results
"""
URL : http://127.0.0.1:8000/items5/
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    }
  ],
  "q": "fixedquery"
}
"""

"""
Below example is of required parameters
"""
@app.get("/items6/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
                    
    if q:
        results.update({"q" : q})
    return results 
"""
Note : you can add None value also in response, because eventually in real world example picklist can have None value
so best way to make required query parameter is by q: Annotated[str | None, Query(min_length=3)]
"""

"""
URL : http://127.0.0.1:8000/items6/
{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "q"
      ],
      "msg": "Field required",
      "input": null
    }
  ]
}
"""   

"""
below is the example of multiple values for query parameter
"""
"""
Note : You can also use list directly instead of list[str]:
"""
@app.get("/items7/")
async def read_items(q: Annotated[list[str] | None, Query()]= None):
    query_items = {"q" : q}
    return query_items
"""
URL : http://127.0.0.1:8000/items7/?q=foo&q=bar
{
  "q": [
    "foo",
    "bar"
  ]
}
"""

"""
Multiple values for query parameter with default values other than None
"""
@app.get("/items8/")
async def read_items(q: Annotated[list[str] | None, Query()]= ["Foo", "Bar"]):
    query_items = {"q" : q}
    return query_items
"""
URL :http://127.0.0.1:8000/items8/
{
  "q": [
    "Foo",
    "Bar"
  ]
}
"""

"""
Additional metadata in Query
"""
@app.get("/items9/")
async def read_items(q: Annotated[str, Query(title="Query string", description="Query to search in the database", min_length=3)]):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
                    
    if q:
        results.update({"q" : q})
    return results 

"""
Alias parameters example and deprecated
"""
@app.get("/items10/")
async def read_items(q: Annotated[str | None, Query(alias="item-query", deprecated=True, include_in_schema=False),] = None):
    results = {
        "items" : [
            {
                "item_id" : "Foo"
            },
            {
                "item_id" : "Bar"
            }
        ]
    }
                    
    if q:
        results.update({"q" : q})
    return results    
"""
URL : http://127.0.0.1:8000/items10/?item-query=sds
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    }
  ],
  "q": "sds"
}
"""

"""
below example is of custom validation
"""
import random
from pydantic import AfterValidator

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_Valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError("Invalid Id Format")
    return id

@app.get("/items11/")
async def read_items(id : Annotated[str | None, AfterValidator(check_Valid_id)] = None):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
        """
        data.items() we get an iterable object with tuples containing the key and value for each dictionary item.
        convert this iterable object into a proper list with list(data.items()).
        Then with random.choice() we can get a random value from the list
        """
    return {
        "id" : id,
        "name" : item
    }

"""
so here in this example id is query parameter and we anotated it with another function
so we can do additional validation
URL :http://127.0.0.1:8000/items11/?id=isbn-9781439512982
{
  "id": "isbn-9781439512982",
  "name": "Isaac Asimov: The Complete Stories, Vol. 2"
}

http://127.0.0.1:8000/items11/?id=igf-9
{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "query",
        "id"
      ],
      "msg": "Value error, Invalid Id Format",
      "input": "igf-9",
      "ctx": {
        "error": {

        }
      }
    }
  ]
}
"""