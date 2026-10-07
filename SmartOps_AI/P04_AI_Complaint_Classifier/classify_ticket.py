from openai import OpenAI
from pydantic import BaseModel, Field
from enum import Enum
from dotenv import load_dotenv
import os

import boto3
import json
from anthropic import AnthropicBedrock
from botocore.config import Config

SYSTEM_PROMPT = """
    you are smartops ticket classifier agent.

    FIRST determine whether the user's message is actually a complaint.
    A complaint means the user is reporting dissatisfaction, a problem, service failure, billing issue, employee or guard issue, delayed response,
    incident, safety concern, or another negative experience.

    Examples of valid complaints:
    - "The guard was 50 minutes late."
    - "I was charged twice."
    - "Nobody responded to my calls."
    - "Your employee was rude."
    - "Our site was left without coverage."

    Examples that are NOT complaints:
    - "What is your price?"
    - "What services do you offer?"
    - "Can I get a quote?"
    - "What time do you open?"
    - "Tell me about SmartOps."

    If the message is NOT a complaint:
    - valid = false
    - explain briefly in validation_reason
    - category = null
    - urgency = null
    - sentiment = null
    - suggested_action = null
    - draft_reply = null
    - do not perform complaint classification

    If the message IS a complaint:
    - valid = true
    - validation_reason = "Valid complaint"

    Classify the complaint into exactly one category:
    - billing: invoices, charges, payments, refunds
    - service_quality: general quality of service issues
    - staff: employee or guard behavior, professionalism, conduct
    - employee: internal employee-related issue
    - response_time: lateness, delayed arrival, slow response, missed timing
    - incident: security incident, safety event, theft, injury, emergency, or property damage
    - other: does not fit the above categories

    Urgency:
    1-3 = low
    4-6 = medium
    7-8 = high
    9-10 = critical or immediate safety/business risk

    Determine sentiment.
    Suggest the appropriate next action in no more than 5 sentences.
    Draft a professional reply, but do NOT claim that an action has already been taken unless the complaint explicitly says it has been taken.

    Do not invent names, dates, actions, or facts.
"""

# 1. ALLOWED CATEGORY VALUES
class Category(str, Enum):
    billing = "billing"
    service_quality = "service_quality"
    staff = "staff"
    employee = "employee"
    response_time = "response_time"
    incident = "incident"
    other = "other"

# 2. ALLOWED SENTIMENT VALUES
class Sentiment(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"

# 3. STRUCTURED OUTPUT SCHEMA
class TicketClassification(BaseModel):
    valid : bool
    validation_reason: str
    category : Category | None = None
    urgency : int | None = Field(default=None, ge=1, le=10)
    sentiment : Sentiment | None = None
    suggested_action : str | None = None
    draft_reply : str | None = None

def policies(key):
    """
    company policies
    """
    POLICIES = {
        "billing": "Refunds are processed within 5 business days.",
        "service_quality": "Service quality complaints must be reviewed by the site manager.",
        "staff": "Staff-related complaints are escalated to operations management.",
        "response_time": "Response-time issues must be acknowledged within 24 hours.",
        "other": "General complaints must be reviewed by the operations team."
    }

    return POLICIES.get(key)

#4. CLASSIFY TICKET FUNCTION
def classify_ticket_groq_gpt(text: str):
    """
    This below code is with OpenAI SDK
    """
    """
    This function will have system prompt which will
    1. classify the complaint
    2. urgency must be between 1 and 10
    3. determine sentiment
    4. suggest the next action
    5. draft a professional reply
    """
    system_prompt = SYSTEM_PROMPT

    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url=os.getenv("GROQ_BASE_URL"),
        timeout=30.0,
        max_retries=0
    )
    model = os.getenv("GROQ_MODEL")

    response = client.responses.parse(
        model=model,
        input=[
            {
                "role" :"system",
                "content" : system_prompt
            },
            {
                "role" : "user",
                "content" : text
            }
        ],
        text_format=TicketClassification
    )

    classify = response.output_parsed
    return classify

#4. CLASSIFY TICKET FUNCTION
def classify_ticket_aws_claude(text: str):
    """
    This below code is with Anthropic SDK
    """
    """
    This function will have system prompt which will
    1. classify the complaint
    2. urgency must be between 1 and 10
    3. determine sentiment
    4. suggest the next action
    5. draft a professional reply
    """
    system_prompt = SYSTEM_PROMPT

    session = boto3.Session() # create a boto3 session to dynamically get and set the region name
    AWS_REGION = session.region_name
    MODEL_NAME = "us.anthropic.claude-sonnet-4-6"

    client = AnthropicBedrock(aws_region=AWS_REGION)
    
    response = client.messages.parse(
        model = MODEL_NAME,
        max_tokens = 20000,
        system = system_prompt,
        messages = [
            {
                "role" : "user",
                "content" : text
            }
        ],
        output_format=TicketClassification
    )

    return response.parsed_output

#4. CLASSIFY TICKET FUNCTION
def classify_ticket_aws_gpt(text: str):
    """
    This below code is with AWS SDK
    """
    """
    This function will have system prompt which will
    1. classify the complaint
    2. urgency must be between 1 and 10
    3. determine sentiment
    4. suggest the next action
    5. draft a professional reply
    """
    system_prompt = SYSTEM_PROMPT

    bedrock = boto3.client( "bedrock-runtime",
        region_name="us-east-1",
        config=Config(
            read_timeout=300,
            connect_timeout=10
        )
    )
    GPT_MODEL = "openai.gpt-oss-120b-1:0"

    schema = TicketClassification.model_json_schema()

    response = bedrock.converse(
        modelId = GPT_MODEL,
        system = [
            {
                "text" : system_prompt
            }
        ],
        messages=[
            {
                "role" : "user",
                "content" : [
                    {
                        "text" : text
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },

        outputConfig={
            "textFormat": {
                "type": "json_schema",
                "structure": {
                    "jsonSchema": {
                        "name": "ticket_classification",
                        "description": "SmartOps complaint classification",
                        "schema": json.dumps(schema)
                    }
                }
            }
        }
    )


    # Get the structured JSON response
    content_blocks = response["output"]["message"]["content"]

    response_text = next(
        (block["text"] for block in content_blocks if "text" in block),
        None
    )

    if response_text is None:
        raise ValueError("No text response returned by GPT-OSS")

    start = response_text.find("{")
    end = response_text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found in GPT-OSS response")

    json_text = response_text[start:end + 1]
    data = json.loads(json_text)
    return TicketClassification.model_validate(data)


def main():
    complaint = """
    The security guard arrived 45 minutes late again.
    This is the second time this month.
    I already spoke with the supervisor last week.
    """
    print("Groq Gpt reply:")
    result = classify_ticket_groq_gpt(complaint)
    print(result.model_dump_json(indent=2))

    print("AWS Claude reply:") 
    result = classify_ticket_aws_claude(complaint)
    print(result.model_dump_json(indent=2))

    print("AWS GPT reply:") 
    result = classify_ticket_aws_gpt(complaint)
    print(result.model_dump_json(indent=2))

if __name__ == "__main__":
    main()

"""
For Groq, we used the OpenAI Python SDK because Groq exposes an OpenAI-compatible API:
For Claude Sonnet on Amazon Bedrock, we used the Anthropic SDK:
"""

"""
Comparison this was my old prompt

    you are smartops ticket classifier agent.

    First read whole complaint and classify the complaint which category, it belongs to
    Analyze the complaint and determine the urgency : 1 indicates low urgency and 10 indicate most urgency
    Determine the sentiment of the user who wrote this complaint.
    Suggest if there are any other action needed to be done in the ticket, or what can be the next steps. This should be in 5 sentence max.
    Draft a professional reply for this complaint, be professional and extract the names, date and important details to use in draft reply.

    Do not create your own wordings or idea apart from the text provided by the user
    If you dont know any answer reply with, "I dont know and need to check with internal team"
    Do not invent your own ideas outside the relevant complaint given by the user.

    Give output as per the structed output given to you.
"""

"""
for new imporved prompt check the code
"""

"""
| Function                       | Model/runtime                                | SDK actually used     |
| ------------------------------ | -------------------------------------------- | --------------------- |
| `classify_ticket_groq_gpt()`   | GPT-OSS through Groq                         | **OpenAI SDK**        |
| `classify_ticket_aws_claude()` | Claude Sonnet through Amazon Bedrock         | **Anthropic SDK**     |
| `classify_ticket_aws_gpt()`    | GPT-OSS-120B through Amazon Bedrock Converse | **AWS SDK (`boto3`)** |

"""