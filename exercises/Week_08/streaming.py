from openai import OpenAI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

class EntitiesModel(BaseModel):
    attributes : list[str]
    colors : list[str]
    animals : list[str]


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
    client.responses.parse() : waits until the entire response is finished, then gives you the result.
    client.responses.stream() : lets you receive the answer piece by piece while the model is generating it.
    This opens a streaming connection to the model.
    """
    with client.responses.stream(
        model = os.getenv(model),
        input=[
            {"role": "system", "content": "Extract entities from the input text"},
            {
                "role": "user",
                "content": "The quick brown fox jumps over the lazy dog with piercing blue eyes",
            },
        ],
        text_format=EntitiesModel,
    ) as stream:
        for event in stream:
            if event.type == "response.refusal.delta":
                print(event.delta, end="")
                """
                Same idea, but now the model is streaming a refusal. as output text but it for refusal stream
                """
            elif event.type == "response.output_text.delta":
                print(event.delta, end="")
                """
                delta means: the new small piece of text that was just generated. see example below
                """
            elif event.type == "response.error":
                print(event.error, end="")
                """
                This means something went wrong during the stream.
                """
            elif event.type == "response.completed":
                print("completed")

        final_response = stream.get_final_response()
        """
        This gives you the complete normal Response object.
        """
        print(final_response.output_text)

main()

"""
event 1 → "Python"
event 2 → " generators"
event 3 → " produce"
event 4 → " values"
event 5 → " one"
event 6 → " at"
event 7 → " a"
event 8 → " time."
"""