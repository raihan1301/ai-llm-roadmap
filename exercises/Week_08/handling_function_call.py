from openai import OpenAI
from dotenv import load_dotenv
import os
import json

"""
below are python functions
"""
def get_weather(city : str):
    """
    this function expects a string for a city

    this is also demo function
    later this could call a real weather api, for right now we fake out the result
    """
    return {
        "city" : city,
        "temperature" : "20 Celcius",
        "condition" : "Sunny"
    }


def send_email(to : str, subject : str, body:str):
    """
    demo function
    later this could use gmail, resend etc and we can write a code to actually send an email
    """

    print("\n--- EMAIL FUNCTION CALLED ---")
    print("To:", to)
    print("Subject:", subject)
    print("Body:", body)

    return {
        "success" : True,
        "message" : f"Demo email prepared for {to}"
    }

"""
below are function router
"""
def call_function(name, args):

    if name == "get_weather":
        return get_weather(**args)

    if name == "send_email":
        return send_email(**args)

    raise ValueError(f"Unknown function : {name}")


"""
Tools we tell the model about and so model can use correctly
"""
responses_tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters" : {
            "type" : "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get weather for"
                }
            },
            "required": ["city"],
            "additionalProperties": False
        },
        "strict" : True
    },
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email to a person.",
        "parameters" : {
            "type": "object",
            "properties" : {
                "to" :{
                    "type" : "string",
                    "description" : "Recipient email address"
                },
                "subject": {
                    "type": "string",
                    "description": "Email subject"
                },
                "body": {
                    "type": "string",
                    "description": "Email body"
                }
            },
            "required": ["to","subject","body"],
            "additionalProperties": False
        },
        "strict" : True
    }
]

def main():
    """
    Main Function
    """

    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url=os.getenv("GROQ_BASE_URL"),
        timeout=30.0,
        max_retries=0
    )
    model = os.getenv("GROQ_MODEL")

    """
    Initial user message
    """
    input_messages = [
        {
            "role": "user",
            "content": ( "What is the weather in Toronto? "
                "Explain the result to me."
            )
        }
    ]

    """
    FIRST MODEL CALL
    """
    response = client.responses.create(
        model=model,
        input=input_messages,
        tools=responses_tools
    )

    """
    SAVE MODEL OUTPUT INTO CONVERSATION
    """
    input_messages += response.output

    """
    LOOK FOR FUNCTION CALLS
    """
    for tool_call in response.output:
        """
        response.output could contain other things, so only process function calls
        """
        if tool_call.type != "function_call":
            continue #this will exit this whole thing and run for another for loop in response output

        name = tool_call.name
        """
        Example: name = "get_weather"
        Arguments arrive as JSON text.
        Example: '{"city":"Toronto"}' json.loads converts it into: {"city": "Toronto"}
        """
        args = json.loads(tool_call.arguments)

        print("\nModel requested function:")
        print("Function:", name)
        print("Arguments:", args)

        """
        ACTUALLY RUN THE PYTHON FUNCTION
        """
        result = call_function(name, args)
        print("Function result:")
        print(result)

        """
        SEND FUNCTION RESULT BACK TO MODEL
        """
        input_messages.append(
            {
                "type" : "function_call_output",
                "call_id" : tool_call.call_id,
                "output" : json.dumps(result)
            }
        )

        """
        SECOND MODEL CALL
        """
        response = client.responses.create(
            model=model,
            input=input_messages,
            tools=responses_tools
        )

        """
        FINAL ANSWER
        """
        print("\nFinal model answer:")
        print(response.output_text)

main()


"""
Plain-English overall logic: We first create two normal Python functions and a list describing those functions to the LLM. 
The user's message is stored in input_messages. The first LLM call decides whether it needs one of our functions. 
We loop through response.output, ignore anything that is not a function_call, extract the function's name and JSON arguments, 
convert those arguments into a Python dictionary using json.loads(), and send them to call_function(). call_function() checks the function name 
and executes the matching Python function using **args. We then store the returned result as a function_call_output, using the same call_id 
so the LLM knows which function request it belongs to. Finally, we send the updated conversation back to the LLM, and now it can use the 
function result to write the final natural-language answer.

This function-calling concept is very important for your roadmap because later your SmartOps agent will use the exact same pattern for things 
such as get_account(), get_complaint_history(), create_task(), and get_contract(). The model does not directly access Supabase—the model 
chooses a tool, your Python code executes it, and the result goes back to the model.
"""

