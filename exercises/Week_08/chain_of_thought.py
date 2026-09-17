from openai import OpenAI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

class Step(BaseModel):
    explanation : str
    output : str

class MathReasoning(BaseModel):
    steps: list[Step]  # new custom datatype we learnt here and passed in list
    final_answer : str
    """
    for steps we have another class for structured output, remember to use BaseModel
    """


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
                "content": "You are a helpful math tutor. Guide the user through the solution step by step."
            },
            {
                "role": "user",
                "content": "how can I solve 8x + 7 = -23"
            }
        ],
        text_format=MathReasoning,
    )

    math_reasoning = response.output_parsed

    print(math_reasoning.model_dump_json(indent=2))
    """
    this will not tell if the model refused or not 
    cannot tell you whether: the model refused, or parsing failed / there was no parsed structured output.
    For refusal handling, you should inspect response.output.
    so we can run a loop below to find it
    """

    if math_reasoning:
        print(math_reasoning.model_dump_json(indent=2))

    else:
        for output in response.output:
            if output.type != "message":
                continue

            for item in output.content:
                if item.type == "refusal":
                    print("Model refused:")
                    print(item.refusal)

"""
response
   ↓
output_parsed
   ↓
Did we get structured data?
   ├── Yes → use math_response
   └── No
         ↓
      check response.output
         ↓
      was there a refusal?

Example      
response.output
message
└── content
    └── refusal
        └── "I'm sorry, I cannot assist with that request."
"""

main()

