"""
We used pydantic model in other files to create structured data,
but we can write text format as well without using the library
"""

from openai import OpenAI
import os
from dotenv import load_dotenv


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

    response = client.responses.create(
        model=os.getenv(model),
        input=[
            {
                "role": "system",
                "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
            },
            {"role": "user", "content": "how can I solve 8x + 7 = -23"},
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "math_response",
                "schema": {
                    "type": "object",
                    "properties": {
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "explanation": {"type": "string"},
                                    "output": {"type": "string"},
                                },
                                "required": ["explanation", "output"],
                                "additionalProperties": False,
                            },
                        },
                        "final_answer": {"type": "string"},
                    },
                    "required": ["steps", "final_answer"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    )

    print(response.output_text)

main()