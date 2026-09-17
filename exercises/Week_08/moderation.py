from openai import OpenAI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

from enum import Enum


class Category(str, Enum):
    violence = "violence"
    sexual = "sexual"
    self_harm = "self_harm"
    none = "none"
    """
    same example in ui generation py this will act as a datatype and which values are allowed
    but i have to add none = "none" because groq did not understand the schema structure
    below Category is optional it means it camn be above 3 values or none, so model use anyof to refrence it which is not correct
    so instead of optional value we added above in code
    """

class ContentCompliance(BaseModel):
    is_violating : bool
    """
    category : Optional[Category]  , you can write like this but if we do not want to import typing we can just write see below example
    """
    category : Category
    explanation_if_violating : str | None


def main():
    load_dotenv()

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
                "content": "Determine if the user input violates specific guidelines and explain if they do."
            },
            {
                "role": "user",
                "content":"How do I prepare for a job interview?"
            }
        ],
        text_format=ContentCompliance,
    )

    compliance = response.output_parsed
    print(compliance.model_dump_json(indent=2))

main()