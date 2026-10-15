from P07_SQL.contract_scorer import (
    Contract_Risk_LLM,
    ContractRiskResult,
    calculate_cost
) 


def test_contract_risk_scorer():

    # -----------------------------
    # Fake contract record
    # -----------------------------
    contract_details = {
        "id": "test-contract-001",
        "agency_id": "test-agency-001",
        "name": "Downtown Office Security",
        "status": "Active",
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "monthly_value": 8500,
        "payment_terms": "Net 30",
        "renewal_number": 0
    }


    # -----------------------------
    # Fake related records
    # -----------------------------
    other_details = {

        "complaints": [
            {
                "id": "complaint-001",
                "contract_id": "test-contract-001",
                "description": "Guard arrived 45 minutes late.",
                "status": "Resolved"
            },
            {
                "id": "complaint-002",
                "contract_id": "test-contract-001",
                "description": "Client reported slow response from supervisor.",
                "status": "Open"
            }
        ],

        "surveys": [
            {
                "id": "survey-001",
                "contract_id": "test-contract-001",
                "nps_score": 6,
                "satisfaction_score": 3,
                "comments": "Service is acceptable but response time needs improvement."
            }
        ],

        "incidents": [
            {
                "id": "incident-001",
                "contract_id": "test-contract-001",
                "severity": "medium",
                "status": "Resolved",
                "description": "Unauthorized visitor entered lobby."
            }
        ],

        "invoices": [
            {
                "id": "invoice-001",
                "contract_id": "test-contract-001",
                "amount": 8500,
                "status": "Paid",
                "days_late": 0
            },
            {
                "id": "invoice-002",
                "contract_id": "test-contract-001",
                "amount": 8500,
                "status": "Overdue",
                "days_late": 14
            }
        ]
    }


    # -----------------------------
    # Call the real LLM
    # -----------------------------
    result, metrics = Contract_Risk_LLM(
        contract_details=contract_details,
        other_details=other_details
    )


    # -----------------------------
    # Calculate actual cost
    # -----------------------------
    cost_usd = calculate_cost(
        metrics.input_tokens,
        metrics.output_tokens
    )


    # -----------------------------
    # Print result
    # -----------------------------
    print("\n" + "=" * 70)

    print("\nCONTRACT RISK RESULT:")
    print(result.model_dump_json(indent=4))

    print("\nLLM METRICS:")
    print("Model:", metrics.model_used)
    print("Input Tokens:", metrics.input_tokens)
    print("Output Tokens:", metrics.output_tokens)
    print("Total Tokens:", metrics.total_tokens)
    print("Cost USD:", cost_usd)

    print("\n" + "=" * 70)


    # -----------------------------
    # Tests
    # -----------------------------

    assert isinstance(result, ContractRiskResult)

    assert result.contract_id == "test-contract-001"

    assert 1 <= result.risk_score <= 10

    assert result.reasoning

    assert len(result.reasoning) > 20

    assert result.suggested_action

    assert len(result.suggested_action) > 20

    assert metrics.input_tokens > 0

    assert metrics.output_tokens > 0

    assert metrics.total_tokens == (
        metrics.input_tokens
        + metrics.output_tokens
    )

    assert cost_usd > 0

if __name__ == "__main__":
    test_contract_risk_scorer()