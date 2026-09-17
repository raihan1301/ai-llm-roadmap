from Project3_SmartOps_Prompt.prompts.email import (EMAIL_SUMMARIZER,
                               PROFESSIONAL_REWRITTER,
                               FOLLOWUP_DRAFTER)

from Project2_AiModels.api_utils import call_llm

def summarize_email(email_text, backend="bedrock"):
    """
    Summarize an incoming or outgoing SmartOps Email
    """

    user = f"""
    Analyze the following email: <email> {email_text} </email>
    """

    response = call_llm(
        system=EMAIL_SUMMARIZER,
        user=user,
        backend=backend
        )
    return response


def professional_rewrite(rough_text, backend="bedrock"):
    """
    Rewrite rough text into professional business communication
    """

    user = f"""
    Rewrite the following text into professional business communication : <rough_text> {rough_text} </rough_text>
    """

    response = call_llm(
        system=EMAIL_SUMMARIZER,
        user=user,
        backend=backend
        )
    return response


def draft_followup(context, backend="bedrock"):
    """
    Draft a follow-up message using the provided business context
    """

    user = f"""
    create a follow-up message using only the following context: <context> {context} </context>
    """

    response = call_llm(
        system=EMAIL_SUMMARIZER,
        user=user,
        backend=backend
        )
    return response


def main():

    """
    Summarize below email
    """
    email = """
        Subject: Guard Coverage for September 10

        Hi Team,

        I wanted to confirm that we need an additional security guard at our Toronto location on September 10 from 6 PM to 11 PM.

        The quoted amount was $350.

        Please confirm by September 8 whether someone will be available.

        Thanks,
        Sarah
    """
    email_summary = summarize_email(email_text=email, backend="bedrock")
    print("\n--- EMAIL SUMMARY ---")
    print(email_summary)


    """
    Professional Rewrite below text
    """
    rough_text = """
        hey sarah we saw your message.

        we are checking if someone is free for september 10. will tell you soon.

        thanks
    """
    rewritten = professional_rewrite(rough_text=rough_text, backend="bedrock")
    print("\n--- PROFESSIONAL REWRITE ---")
    print(rewritten)


    """
    Follow Up Draft message for below text
    """
    context = """
        Client: Sarah Smith
        Company: ABC Security

        Sarah requested an additional security guard for the Toronto site on September 10 between 6 PM and 11 PM.

        SmartOps previously told Sarah that the operations team would check guard availability.

        No confirmation has been sent yet.

        Sarah requested confirmation by September 8.
    """
    followup = draft_followup(context=context, backend="bedrock")
    print("\n--- FOLLOW-UP DRAFT ---")
    print(followup)


if __name__ == "__main__":
    main()
