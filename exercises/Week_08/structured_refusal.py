from openai import OpenAI
import os
from dotenv import load_dotenv

from pydantic import BaseModel

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


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
                "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
            },
            {"role": "user", "content": "how can I solve 8x + 7 = -23,"},
        ],
        text_format=MathReasoning,
    )

    print(response.model_dump_json(indent=2))
    """
    This above print is The longer loop version is useful only when you want to inspect each raw output item yourself, 
    for example to separately handle a refusal:
    """

    for output in response.output:
        if output.type != "message":
            continue

        for item in output.content:
            if item.type == "refusal":
                # If the model refuses to respond, you will get a refusal message
                print(item.refusal)
                continue

            if not item.parsed:
                raise Exception("Could not parse response")

            print(item.parsed.model_dump_json(indent=2))
            """
            cannot tell you whether: the model refused, or parsing failed / there was no parsed structured output.
            For refusal handling, you should inspect response.output.
            """

main()