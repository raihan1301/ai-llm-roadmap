from Project3_SmartOps_Prompt.prompts.survey import (NPS_RESPONSE_GENERATOR)

from Project2_AiModels.api_utils import call_llm


def generate_nps_response(survey_feedback,backend="bedrock"):
    """
    Analyze survey/NPS feedback and generate an appropriate response.
    """

    user = f"""
    Analyze the following customer survey or NPS feedback: <survey_feedback> {survey_feedback} </survey_feedback>
    """

    response = call_llm(
        system=NPS_RESPONSE_GENERATOR,
        user=user,
        backend=backend
        )
    return response


def main():
    survey_feedback  = """
        Company: ABC Security
        Contract Number: SEC-2026-104

        Contract renewal is due in December 2026.

        During the current contract term:
            - Guards arrived late 4 times.
            - There were 2 client complaints.
            - One complaint took 8 days to resolve.
            - The second complaint was resolved within 1 day.
            - There was one minor incident involving an unlocked entrance.
            - Average response time to client emails was 18 hours.

        The client has mentioned concerns about guard punctuality during the last account review.
    """

    result = generate_nps_response(survey_feedback=survey_feedback , backend="bedrock")

    print("\n--- NPS / SURVEY ANALYSIS ---")
    print(result)


if __name__ == "__main__":
    main()