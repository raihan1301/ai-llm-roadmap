from supabase import create_client
from dotenv import load_dotenv
import os

from classify_ticket import classify_ticket_aws_claude
from classify_ticket import classify_ticket_aws_gpt

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
        .limit(5)
        .execute()
    )

    comparison_results = []

    for complaint in response.data:

        complaint_text = complaint["description"]

        print("\nORIGINAL COMPLAINT:")
        print(complaint_text)

        claude_result = classify_ticket_aws_claude(complaint_text)
        gpt_result = classify_ticket_aws_gpt(complaint_text)

        comparison_results.append({
            "complaint": complaint_text,
            "gpt": gpt_result.model_dump(),
            "claude": claude_result.model_dump()
        })
        print("\nAI CLASSIFICATION:")
        print(comparison_results[-1])
        print("\n" + "=" * 70)

if __name__ == "__main__":
    main()