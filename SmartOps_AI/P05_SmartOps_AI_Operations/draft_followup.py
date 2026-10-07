"""
account_id
   ↓
accounts table
   ↓
related contracts
related complaints
related surveys
possibly incidents
   ↓
build account context
   ↓
LLM drafts a follow-up message
   ↓
return subject + message + reason/context

from account id, draft a email which tells how our service experience, based on how many contracts renewals, complaints, surveys, incidents
"""

from supabase import create_client
from dotenv import load_dotenv
import json
from pydantic import BaseModel
from anthropic import AnthropicBedrock
import os
import boto3

"""
This is the pydantic structure for model LLM
"""
class FollowupDraftAI(BaseModel):
    followup_type : str
    subject : str
    message : str

"""
This will be final output structure include all the values
"""
class FollowupDraft(BaseModel):
    valid: bool
    contract_id: str | None = None
    followup_type : str | None = None
    subject : str | None = None
    message : str | None = None
    reason : str | None = None

"""
This method will will create followup email, it will recieve contract details as parameter
"""
def followup_draft_email(contract_details, other_details):

    system_prompt = f"""
    You are SmartOps Follow up email agent.
    Your job is to create a follow up message to client, asking did they like our service

    Step 1:
        from {contract_details} extract important contract information. 
        you should extract contract start date, end date, contract value, payment terms, renewal terms
        you should also extract any other important information you found in contract_details
        
    Step 2:
        we also provided you with {other_details} : this contains if there is any survey, incident, complaints related to this contract
        analyze and extract all the important information
    
    Step 3:
        Create a concise professional service follow-up email.
        Use the contract, survey, complaint, and incident information as context, 
            but only mention details that are useful and appropriate for the client.
        Do not automatically repeat contract value, internal IDs, internal notes, or administrative fields.
        Mention significant service feedback, complaints, or incidents only when they are relevant to the service check-in.
        Ask how the client feels about the service and whether they have any questions, concerns, or feedback.
    
    Step 4: 
        Subject line should include the contract/site name when available.

    Do not invent your own information. all the info should come from the text given to you
    Do not miss any important information.
    do not suggest any action has already been started.
    If you dont know anything output "Dont know" for that particular thing
    """

    content = f"""
    CONTRACT : {json.dumps(contract_details, indent=2)}

    RELATED INFORMATION : {json.dumps(other_details, indent=2)}
    """

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
                "content" : content
            }
        ],
        output_format=FollowupDraftAI
    )
    
    return response.parsed_output


"""
This method will get the contract from supabase
"""
def get_contract(contract_id):
    load_dotenv()
        
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
        
    response = (
        supabase
        .table("contracts")
        .select("*")
        .eq("id", contract_id)
        .maybe_single()
        .execute()
    )

    contract = response.data

    if not contract:
        return None

    return contract

"""
This will get other information for that contract
"""
def get_other_details(contract_id):
    load_dotenv()
        
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
        
    survey_response = (
        supabase
        .table("surveys")
        .select("*")
        .eq("contract_id", contract_id)
        .execute()
    )

    complaint_response = (
        supabase
        .table("complaints")
        .select("*")
        .eq("contract_id", contract_id)
        .execute()
    )

    incident_response = (
        supabase
        .table("incidents")
        .select("*")
        .eq("contract_id", contract_id)
        .execute()
    )

    return {
        "surveys" : survey_response.data,
        "complaints" : complaint_response.data,
        "incidents" : incident_response.data
    }


def main():
    contract_id = input("Enter Contract id : ")
    """
    right now it is by terminal, in smartops we can automate that, as soon as complaint lands
    or user click button it will fetch the complaint id, for testing we are using input mechanism now
    """

    contract_description = get_contract(contract_id)
    print("\n contract_description:")
    print(contract_description)

    if not contract_description:
        result = FollowupDraft(
            valid=False,
            contract_id=contract_id,
            reason="contract not found."
        )

    else:
        other_details = get_other_details(contract_id)
        print("\n other_details:")
        print(other_details)

        draft_email = followup_draft_email(contract_details=contract_description, other_details=other_details)

        result = FollowupDraft(
            valid=True,
            contract_id=contract_id,
            followup_type = draft_email.followup_type,
            subject = draft_email.subject,
            message = draft_email.message
        )

    draft_email_json = json.dumps(result.model_dump(mode="json"),indent = 4)

    print("\n AI Result:")
    print(draft_email_json)


if __name__ == "__main__":
        main()

