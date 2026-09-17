from Project3_SmartOps_Prompt.prompts.meeting import (MEETING_NOTES_FORMATTER)

from Project2_AiModels.api_utils import call_llm


def format_meeting_notes(meeting_content,backend="bedrock"):
    """
    Convert raw meeting notes/ transcript into structured meeting notes
    """

    user = f"""
    Analyze and format the following meeting content: <meeting_content> {meeting_content} </meeting_content>
    """

    response = call_llm(
        system=MEETING_NOTES_FORMATTER,
        user=user,
        backend=backend
        )
    return response


def main():
    meeting_content = """
        Meeting with ABC Security on September 7.

        Sarah mentioned that two guards were late last month. The client is concerned about weekend coverage.

        John from operations agreed to review the weekend schedule and provide an updated staffing plan by September 10.

        Sarah also requested monthly attendance reports.

        Everyone agreed to meet again on September 15 at 2 PM to review the new staffing plan.
    """

    result = format_meeting_notes(meeting_content=meeting_content, backend="bedrock")

    print("\n--- MEETING NOTES ---")
    print(result)


if __name__ == "__main__":
    main()