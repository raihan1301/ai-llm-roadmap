"""
This will show to handle edge case, like model did not generate a valid response that matches the json schema
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

    try:
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
                    "strict": True,
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
                },
            },
            max_output_tokens=50,
        )

        if (
            response.status == "incomplete"
            and response.incomplete_details.reason == "max_output_tokens"
        ):
            raise Exception("Incomplete response")

        message = None

        for item in response.output:
            if item.type == "message":
                message = item
                break

        math_response = None

        if message and message.content:
            math_response = message.content[0]

        """
        also for line 70 to 80 we can write below code as well 

        message = next(
            (item for item in response.output if item.type == "message"),
            None
        )

        math_response = message.content[0] if message and message.content else None
        """

        if not math_response:
            raise Exception("No response content")

        if math_response.type == "refusal":
            print(math_response.refusal)
        elif math_response.type == "output_text":
            print(math_response.text)
        else:
            raise Exception("No response content")
    except Exception as e:
        # handle errors like finish_reason, refusal, content_filter, etc.
        print(e)


main()