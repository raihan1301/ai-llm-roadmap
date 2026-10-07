"""
complaint text
    ↓
validate_complaint()
    ↓
if invalid → stop early
    ↓
classify_ticket()
    ↓
category + urgency + sentiment + suggested_action
    ↓
POLICIES[category]
    ↓
draft_policy_reply()
    ↓
final v2 result
"""

from supabase import create_client
from dotenv import load_dotenv
import json
from pydantic import BaseModel
from anthropic import AnthropicBedrock
import os
import boto3

from P04_AI_Complaint_Classifier.classify_ticket import classify_ticket_aws_claude , policies


"""
classify ticket version 2 :
It will validate the complaint and than classify it into the result as well as lookup policies to draft the reply
"""
def classify_ticket_v2(text):

    #step 1 : Validation
    validate, reason = validate_safety(text)
    if not validate:
        return TicketClassificationV2(
            valid = False,
            reason = reason
        )

    #step 2 : classify the ticket in category, urgency, sentiment, suggested_action
    classify = classify_ticket_aws_claude(text)
    if not classify.valid:
        return TicketClassificationV2(
            valid = False,
            reason = classify.validation_reason
        )

    #Step 3: get the company policy
    policy = policies(classify.category)

    #Step 4: draft the reply
    draft_reply = draft_policy_reply(text, classify, policy)

    return TicketClassificationV2(
        valid = True,
        category = classify.category,
        urgency = classify.urgency,
        sentiment = classify.sentiment,
        suggested_action = classify.suggested_action,
        policy = policy,
        draft_reply = draft_reply
    )

"""
Structured Model for output Ticket Classification
"""
class TicketClassificationV2(BaseModel):
    valid: bool
    reason : str | None = None
    category: str | None = None
    urgency: int | None = None
    sentiment: str | None = None
    suggested_action: str | None = None
    policy: str | None = None
    draft_reply: str | None = None

"""
This function will validate the complaint if its safe or not
"""
def validate_safety(text):

    bedrock = boto3.client(
        "bedrock-runtime",
        region_name="us-east-1"
    )

    response = bedrock.apply_guardrail(
        guardrailIdentifier="a1m0butw7915",
        guardrailVersion="DRAFT",
        source="INPUT",
        content=[
            {
                "text": 
                {
                    "text" : text
                }
            }
        ],
        outputScope="FULL"
        )
  
    moderation_output = response["action"] == "GUARDRAIL_INTERVENED"

    if moderation_output: 
        # if blocked
        reason = response.get("actionReason","Request was blocked by the safety guardrail.")
        return False, reason

    return True, "Request passed the safety check."

"""
This function will draft reply based on company policies
"""
def draft_policy_reply(text, classification, policy):

    """
    Now we have created a draft reply in my previous code, but instead of upating that, we can just remove it from dumping
    """
    classification_context = classification.model_dump(exclude={"draft_reply"})

    system_prompt = f"""
        you are smartops reply agent.
    
        Draft a professional reply, but do NOT claim that an action has already been taken unless the complaint explicitly says it has been taken.
        In your reply, please take care of company policy and use company policy to answer the request : {policy}

        for context, here is the important details about the complaint, this details include, ticket category, urgency, sentiment and suggested action
        ignore the draft reply from this response and create your own draft reply using this details and company policy : {classification_context}

        for your reference i am including the complaint text as well : {text}
        
        IMPORTANT:
        The suggested_action contains recommended future actions.
        It does NOT mean those actions have already happened.

        Do not invent names, dates, actions, or facts.

        return only the draft reply nothing else
        Do not include JSON, labels, keys, or markdown formatting.
    """

    session = boto3.Session() # create a boto3 session to dynamically get and set the region name

    AWS_REGION = session.region_name
    MODEL_NAME = "us.anthropic.claude-sonnet-4-6"
    
    client = AnthropicBedrock(aws_region=AWS_REGION)

    """
    we cannot use client.messages.parse() here because parse is used for pydantic structure
    for this see the example where we classify the ticket using Basemodel in classify_ticket.py
    so here we only need to see the draft reply so we will use client.messages.create()
    """
    response = client.messages.create(
        model = MODEL_NAME,
        max_tokens = 20000,
        system = system_prompt,
        messages = [
            {
                "role" : "user",
                "content" : text
            }
        ],
    )

    return response.content[0].text

"""
we can keep the parse but than we have to define this structure
class DraftReply(BaseModel):
    draft_reply: str
"""


def main():
    load_dotenv()
    
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
    
    response = (
        supabase
        .table("complaints")
        .select("*")
        .order("id")
        .limit(2)
        .execute()
    )

    complaints_to_test = response.data + [
        {
            "description": "What is the price of your security service?",
            "test_case": "Not a complaint"
        },
        {
            "description": "Can I get a quote for 3 security guards?",
            "test_case": "Not a complaint"
        }
    ]
    
    for complaint in complaints_to_test:
    
        complaint_text = complaint["description"]
    
        print("\nORIGINAL COMPLAINT:")
        print(complaint_text)
    
        complaint_result = classify_ticket_v2(complaint_text)

        print("\n AI Result:")
        print(json.dumps
                (
                    complaint_result.model_dump(mode="json"),
                    indent = 4
                )
            )
        print("\n" + "=" * 70)


if __name__ == "__main__":
        main()