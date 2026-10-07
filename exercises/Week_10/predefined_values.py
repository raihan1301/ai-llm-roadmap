from fastapi import FastAPI
from enum import Enum

"""
here we are creating a data type predefined values
so it can be used in below methods
"""
"""
Enum says: Only these predefined values are allowed.
The str part in: tells Python/FastAPI that the Enum's values are string-based
"""
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "res"
    lenet = "lenet"

"""
resnet is the Enum member name, while "res" is the actual value accepted from the URL.
So when you call: /models/res below
FastAPI convert "res" into ModelName.resnet
That means inside your function: model_name == ModelName.resnet is True
"""
app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):

    """
    here we have pass that class as data type for model_name variable
    """

    if model_name is ModelName.alexnet:
        return {"model_name" : model_name, "message" : "Deep Learning FTW"}

    if model_name.value == "res":
        return {"model_name" : model_name, "model_name_name": model_name.name, "message" : "Have some residuals"}

    return {"model_name" : model_name, "message" : "LeCNN all the images"}

"""
remember in above model i tried to enter alexnet as model_name it worked
but when i tried to add "res" as model_name i got this error : "msg": "Input should be 'alexnet', 'res' or 'lenet'"
It means we have to pass the value in model_name
"""

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}