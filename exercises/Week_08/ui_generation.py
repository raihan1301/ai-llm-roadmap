from openai import OpenAI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

from enum import Enum
from typing import List

"""
Enum lets you define a fixed set of allowed values.
"""
class UiType(str, Enum):
    """
    Reason class UiType(str, Enum): and not just: class UiType(Enum):
    is that the values should behave like strings when converted to JSON.
    """
    div = "div"
    button = "button"
    header = "header"
    section = "section"
    field = "field"
    form = "form"
"""
UiType - this create custom datatype and what values are allowed inside them
we will use this datatype below
"""

class Attribute(BaseModel):
    name : str
    value : str

class UI(BaseModel):
    type : UiType  # new custom datatype we learnt here
    """
    So here we are saying type should be of UiType datatype only and the valid value are given in above class when we declared it
    type = "button" is valid type, type = "form" is valid, type = "banana" is not valid
    That's useful for Structured Outputs because the LLM cannot invent random UI types.
    """
    label : str
    children : List["UI"]
    """
    This means we are using recursive function,
    In summary UI element which is children here can be a list of other UI elements
    so for example a record contains type, label, children [ and inside the children there can be type, label, children [], attributes], attributes
    see the output and That's why "UI" is written inside quotes.
    """
    attributes : List[Attribute]

class Response(BaseModel):
    ui : UI
    """
    This is just the outer wrapper.
    like it wrap the whole json with outer key ui
    Response
    └── ui: UI
        ├── type: UiType
        ├── label: str
        ├── children: list[UI]
        └── attributes: list[Attribute]
                        ├── name: str
                        └── value: str
    """


def main():
    load_dotenv()

    UI.model_rebuild()
    """
    we need above line because UI references itself here: 
    Pydantic sometimes needs to resolve that reference after the class has finished being defined.
    model_rebuild() basically says: Pydantic, the UI class now exists. Rebuild the schema and resolve "UI" correctly."
    and this allows the recursive structure
    """

    api_key = "GROQ_API_KEY"
    base_url = "GROQ_BASE_URL"
    model = "GROQ_MODEL"

    client = OpenAI(
        api_key=os.getenv(api_key),
        base_url=os.getenv(base_url),
        timeout=30.0,
        max_retries=0
    )

    response = client.responses.parse(
        model=os.getenv(model),
        input=[
            {
                "role": "system",
                "content": "You are a UI generator AI. Convert the user input into a UI."
            },
            {
                "role": "user",
                "content":"Make a User Profile Form."
            }
        ],
        text_format=Response,
    )

    ui = response.output_parsed
    print(ui.model_dump_json(indent=2))

main()