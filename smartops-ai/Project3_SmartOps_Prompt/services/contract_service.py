from Project3_SmartOps_Prompt.prompts.contract import (CONTRACT_RISK_EXTRACTOR)

from Project2_AiModels.api_utils import call_llm


def extract_contract_risk(contract_context,backend="bedrock"):
    """
    Analyze contract/business context and identify renewal risks.
    """

    user = f"""
    Analyze the following contract and business information: <contract_context> {contract_context} </contract_context>
    """

    response = call_llm(
        system=CONTRACT_RISK_EXTRACTOR,
        user=user,
        backend=backend
        )
    return response


def main():
    contract_context = """
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

    result = extract_contract_risk(contract_context=contract_context, backend="bedrock")

    print("\n--- CONTRACT RISK ---")
    print(result)


if __name__ == "__main__":
    main()