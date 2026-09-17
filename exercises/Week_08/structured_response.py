from openai import OpenAI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

"""
below is basemodel from pydantic
this is used to create structured output, how it can be used see below at last for an example
"""
class CalendarEvent(BaseModel):
    name : str
    date : str
    participants : list[str]

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
    """
    client is use to connect the api key and url to use the model
    """
    
    response = client.responses.parse(
        model=os.getenv(model),
        input=[
            {
                "role": "system",
                "content": "Extract the event information"
            },
            {
                "role": "user",
                "content": "Alice and Bob are going to a science fair on Friday."
            }
        ],
        text_format=CalendarEvent,
    )

    event = response.output_parsed
    print(event)

"""
BaseModel
   ↓
Define exactly what fields you want
   ↓
Give each field a type
   ↓
LLM must return data matching that structure
"""

main()

"""
Example for different use of pydantic model

from pydantic import BaseModel

class ComplaintClassification(BaseModel):
    category: str
    urgency: int
    sentiment: str
    suggested_action: str
    draft_reply: str

response = client.responses.parse(
    model=model,
    input=[...],
    text_format=ComplaintClassification
)

result = response.output_parsed
"""