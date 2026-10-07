"""
complaint_id
    ↓
Supabase complaints table
    ↓
Find complaint by id
    ↓
If not found → return valid=False
    ↓
Send complaint text/details to Claude
    ↓
Return structured summary
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
class ComplaintSummaryAI(BaseModel):
    summary: str
    key_issue: str
    severity: str
    reason: str

"""
This will be final output structure include all the values
"""
class ComplaintSummary(BaseModel):
    valid: bool
    complaint_id: str | None = None
    summary: str | None = None
    key_issue: str | None = None
    severity: str | None = None
    reason: str | None = None

"""
This method will summarize the complaint and it will recieve a complaint in parameter
"""
def summarize_complaint(complaint):

    system_prompt = """
    You are SmartOps complaint summarizer agent

    Your job is to analyze the whole complaint and than do the following steps:
    
    Step 1:
        Summarize the complaint provided as a user input to you in 4 to 5 sentences.
        In summary include all the main details in the complaint : name, location, date, staff, reason, etc.
        If the complaint is wrong and important details are missing out, you can summarize the complaint in 8 to 10 sentences.
    
    Step 2:
        Identify the main issue of the complaint
    
    Step 3:
        When you analyze the complaint, check for the severity, how urgent this complaint is, below is the category for severity
        Critical - it needs urgent action
        High - Action needs to be taken in next 2 hour
        Medium - Action needs to be taken by tomorrow
        Low - Action will be taken in 2-3 business days

    Do not invent your own information. all the summary and response should be from orignal complaint
    Do not miss any important information from the complaint
    do not suggest any action has already been started.
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
                "content" : complaint
            }
        ],
        output_format=ComplaintSummaryAI
    )
    
    return response.parsed_output


"""
This method will get the complaint from supabase
"""
def get_complaint(complaint_id):
    load_dotenv()
        
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
        
    response = (
        supabase
        .table("complaints")
        .select("*")
        .eq("id", complaint_id)
        .execute()
    )

    complaints = response.data

    if not complaints:
        return None

    for complaint in complaints:

        print("\nORIGINAL COMPLAINT:")
        print(complaint)

        
        complaint_text = complaint["description"]

        print("\nORIGINAL COMPLAINT:")
        print(complaint_text)

        return complaint_text



def main():
    complaint_id = input("Enter complaint id : ")
    """
    right now it is by terminal, in smartops we can automate that, as soon as complaint lands
    or user click button it will fetch the complaint id, for testing we are using input mechanism now
    """

    complaint_description = get_complaint(complaint_id)
    print("complaint_Description: ", complaint_description)
    if not complaint_description:
        result = ComplaintSummary(
            valid=False,
            complaint_id=complaint_id,
            reason="Complaint not found."
        )

    else:
        complaint_summary = summarize_complaint(complaint_description)

        result = ComplaintSummary(
            valid=True,
            complaint_id=complaint_id,
            summary=complaint_summary.summary,
            key_issue=complaint_summary.key_issue,
            severity=complaint_summary.severity,
            reason=complaint_summary.reason
        )
    complaint_json = json.dumps(result.model_dump(mode="json"),indent = 4)

    print("\n AI Result:")
    print(complaint_json)


if __name__ == "__main__":
        main()

