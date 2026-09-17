from Project3_SmartOps_Prompt.prompts.complaint import (SENTIMENT_ANALYZER,
                               ACTION_EXTRACTOR,
                               URGENCY_SCORER,
                               COMPLAINT_CATEGORIZER)

from Project2_AiModels.api_utils import call_llm


def sentiment_analyzer(complaint, backend ="bedrock"):
    """
    analyze the customers sentiment from a complaint
    """
    response = call_llm(
        system = SENTIMENT_ANALYZER,
        user = complaint,
        backend = backend
    )
    return response


def action_extractor(complaint, backend="bedrock"):
    """
    Extract completed or requested actions from a complaint
    """
    response = call_llm(
        system=ACTION_EXTRACTOR,
        user=complaint,
        backend=backend
    )
    return response


def urgency_scorer(complaint, setiment_result, action_result, backend="bedrock"):
    """
    calculate complaint urgenncy based on orignal complaint and sentiment as well as action result
    """
    user = f"""
    orignal complaint : <complaint> {complaint} </complaint>
    Sentiment Analysis : <sentiment> {setiment_result} </sentiment>
    Action Analysis : <actions> {action_result} </actions>
    """

    response = call_llm(
            system=URGENCY_SCORER,
            user=user,
            backend=backend
        )
    return response
    

def complaint_categorize(complaint, setiment_result, action_result, urgency_result, backend="bedrock"):
    """
    combine all the result and categorize the complaint with summary
    """
    user = f"""
    orignal complaint : <complaint> {complaint} </complaint>
    Sentiment Analysis : <sentiment> {setiment_result} </sentiment>
    Action Analysis : <actions> {action_result} </actions>
    Urgency Analysis : <urgency> {urgency_result} </urgency>
    """

    response = call_llm(
                system=COMPLAINT_CATEGORIZER,
                user=user,
                backend=backend
            )
    return response

def analyze_complaint(complaint, backend="bedrock"):
    """
    Run the complete SmartOps complaint analysis pipeline.
    """

    sentiment_result = sentiment_analyzer(complaint=complaint, backend=backend)
    action_result = action_extractor(complaint=complaint, backend=backend)
    urgency_result = urgency_scorer(complaint=complaint, setiment_result=sentiment_result, action_result=action_result, backend=backend)
    final_result =  complaint_categorize(complaint=complaint, setiment_result=sentiment_result, action_result=action_result, urgency_result=urgency_result, backend=backend)
    
    return {
        "sentiment_analysis": sentiment_result,
        "action_analysis": action_result,
        "urgency_analysis": urgency_result,
        "final_analysis": final_result
    }


def main():
    complaint = """
    ABC Security reported that guard John arrived 45 minutes
    late for his scheduled shift.

    The client, Sarah Smith, said this is the second time it
    has happened this month. She called the site supervisor,
    who contacted the guard and asked him to report immediately.

    Sarah is frustrated and requested that SmartOps investigate
    the repeated lateness and provide a replacement guard if
    this happens again.
    """

    result = analyze_complaint(complaint=complaint, backend="bedrock")

    print("\n--- SENTIMENT ---")
    print(result["sentiment_analysis"])

    print("\n--- ACTIONS ---")
    print(result["action_analysis"])

    print("\n--- URGENCY ---")
    print(result["urgency_analysis"])

    print("\n--- FINAL COMPLAINT ANALYSIS ---")
    print(result["final_analysis"])

if __name__ == "__main__":
    main()


"""
ok now to run it we do not have to be inside this directory, we have to be at smartops-ai

so to run this file 
python -m Project3_SmartOps_Prompt.services.complaint_services
"""