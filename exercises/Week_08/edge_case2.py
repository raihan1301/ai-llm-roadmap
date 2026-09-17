from openai import OpenAI
import os
from dotenv import load_dotenv

def main():

    we_did_not_specify_stop_tokens = True

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
                    "content": "You are a helpful assistant designed to output JSON.",
                },
                {
                    "role": "user",
                    "content": 'Who won the World Series in 2020? Respond as {"winner": "team name"}.',
                },
            ],
            text={"format": {"type": "json_object"}},
        )

        message = next((item for item in response.output if item.type == "message"), None)
        message_content = message.content[0] if message and message.content else None

        # Check if the conversation was too long for the context window, resulting in incomplete JSON
        if ( response.status == "incomplete" and response.incomplete_details.reason == "max_output_tokens"):
            raise RuntimeError("The response was truncated before the JSON completed.")

        # Check if the OpenAI safety system refused the request and generated a refusal instead
        if message_content and message_content.type == "refusal":
            print(message_content.refusal)

        # Check if the model's output included restricted content, so the generation of JSON was halted and may be partial
        if ( response.status == "incomplete" and response.incomplete_details.reason == "content_filter"):
            raise RuntimeError("The response was interrupted by the content filter.")

        if response.status == "completed":
            """
            In this case the model has either successfully finished generating the JSON object according to your schema, 
            or the model generated one of the tokens you provided as a "stop token"
            """
            if we_did_not_specify_stop_tokens:
                """
                If you didn't specify any stop tokens, then the generation is complete and the content key will contain the serialized JSON object
                This will parse successfully and should now contain  "{"winner": "Los Angeles Dodgers"}"
                """
                print(response.output_text)

    except Exception as e:
    # Your code should handle errors here, for example a network error calling the API
        print(e)

main()

