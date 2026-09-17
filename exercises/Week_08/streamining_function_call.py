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

"""
below are function router
"""
def call_function(name, args):

    if name == "get_weather":
        return get_weather(**args)

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
    },
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
    FIRST MODEL CALL - Stream function call
    """
    response = client.responses.create(
        model=model,
        input=input_messages,
        tools=responses_tools,
        stream = True,
    )

    """
    We use output_index as the key because the model could potentially request more than one function.
    """
    final_tool_calls = {}

    """
    READ STREAM EVENTS
    """
    for event in response:
        """
        A new output item has started.
        """
        if event.type == "response.output_item.added":
            """
            We only care about function calls here.
            """
            if event.item.type == "function_call":
                final_tool_calls[event.output_index] = {
                    "type": "function_call",
                    "id": event.item.id,
                    "call_id": event.item.call_id,
                    "name": event.item.name,
                    "arguments" : ""                    
                }
                """
                Arguments are streamed piece by piece, so start with an empty string. above
                """

        elif event.type == "response.function_call_arguments.delta" :
            """
            Function arguments are arriving piece by piece.
            """
            index = event.output_index

            if index in final_tool_calls:
                final_tool_calls[index]["arguments"] += event.delta

        elif event.type == "response.error":
            print("Streaming error:", event.error)


    """
    SEE THE COMPLETED FUNCTION CALL
    """
    print("\nCompleted tool calls:")

    for index in sorted(final_tool_calls):
        tool_call = final_tool_calls[index]

        print(json.dumps(tool_call, indent=2))


    """
    EXECUTE EACH REQUESTED FUNCTION
    """
    for index in sorted(final_tool_calls):
        tool_call = final_tool_calls[index]

        """
        First save the model's function request into conversation history.
        """
        input_messages.append(tool_call)

        name = tool_call["name"]
        args = json.loads(tool_call["arguments"])
        """
        Arguments currently look like: '{"location":"Paris, France"}' Convert JSON string -> Python dictionary.
        """

        print("\nCalling Python function:")
        print("Function:", name)
        print("Arguments:", args)

        """
        Actually execute our Python function.
        """
        result = call_function(name, args)
        print("Function result:")
        print(result)

        """
        SEND FUNCTION RESULT BACK TO MODEL
        """
        input_messages.append(
            {
                "type": "function_call_output",
                "call_id": tool_call["call_id"],
                "output": json.dumps(result)
            }
        )

    """
    SECOND MODEL CALL — STREAM FINAL ANSWER
    """
    print("\nFinal model answer:")

    final_response = client.responses.create(
        model=model,
        input=input_messages,
        tools=responses_tools,
        stream=True,
    )

    for event in final_response:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)

        elif event.type == "response.refusal.delta":
            print(event.delta, end="", flush=True)

        elif event.type == "response.error":
            print("\nError:", event.error)

        elif event.type == "response.completed":
            print("\n\nCompleted.")


main()

"""
TIP : The confusing part is probably this section: final_tool_calls = {}
Because during streaming, the model might not send: {"location": "Paris, France"}
we might recieve :
event 1: "{"
event 2: "\"location\""
event 3: ":"
event 4: "\"Paris"
event 5: ", France\""
event 6: "}"
"""

"""
One important difference from your non-streaming function-calling code is that previously you could simply do:
for tool_call in response.output: because the response was already complete.
With streaming, the function call is still being constructed while you receive it, 
so you first have to collect the deltas, then execute the completed function call.
"""

"""
Code Explanation : 
We first create an empty dictionary called final_tool_calls. As the model streams events, response.output_item.added tells us that a 
function call has started, so we create an entry for it using output_index as the key. Each response.function_call_arguments.delta 
contains another small piece of the arguments, so we append that piece to the existing arguments string. After the stream finishes, 
we loop through the completed function calls, convert each argument string into a Python dictionary with json.loads(), 
run the matching Python function, and append both the function request and its result to input_messages. Finally, 
we make a second model call and stream the model's natural-language answer back to the terminal.
"""

