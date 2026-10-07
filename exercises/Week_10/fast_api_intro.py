from fastapi import FastAPI

app = FastAPI() 
"""
create a FastAPI "instance
app variable will be an "instance" of the class FastAPI.
This will be the main point of interaction to create all your API.
"""


"""
"Path" here refers to the last part of the URL starting from the first /
example : https://example.com/items/foo
...the path would be: /items/foo

you can also see the operation : 
POST, GET, PUT, DELETE, OPTIONS, HEAD, PATCH, TRACE
each http method is called an operation
"""
@app.get("/")
async def root():
    return {"message" : "hello world"}


"""
In Summary:
path: is /.
operation: is get.
function: is the function below the "decorator" (below @app.get("/")).
"""

"""
To deploy:
Deploy it with one command: fastapi deploy
"""