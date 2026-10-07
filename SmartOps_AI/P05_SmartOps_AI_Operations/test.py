
"""
Week 9 - SmartOps AI Ops Module
12 pytest tests total:
3 classify_ticket_v2
3 summarize_complaint
3 extract_contract_data
3 draft_followup

These are unit tests. They mock AWS/Claude and Supabase.
If your filenames differ, update only the 4 module paths below.
"""

import importlib
from types import SimpleNamespace
import pytest

classify_mod = importlib.import_module("Project5_SmartOps_classify.classify_ticket_v2")
summary_mod = importlib.import_module("Project5_SmartOps_classify.summarize_complaint")
contract_mod = importlib.import_module("Project5_SmartOps_classify.extract_contract_data")
followup_mod = importlib.import_module("Project5_SmartOps_classify.draft_followup")


class FakeQuery:
    def __init__(self, data):
        self.data = data
        self.single = False

    def select(self, *args, **kwargs):
        return self

    def eq(self, *args, **kwargs):
        return self

    def order(self, *args, **kwargs):
        return self

    def limit(self, *args, **kwargs):
        return self

    def maybe_single(self):
        self.single = True
        return self

    def execute(self):
        data = self.data
        if self.single and isinstance(data, list):
            data = data[0] if data else None
        return SimpleNamespace(data=data)


class FakeSupabase:
    def __init__(self, table_data):
        self.table_data = table_data

    def table(self, name):
        return FakeQuery(self.table_data.get(name, []))


class FakeMessages:
    def __init__(self, parsed_output):
        self.parsed_output = parsed_output

    def parse(self, **kwargs):
        return SimpleNamespace(parsed_output=self.parsed_output)


class FakeAnthropicClient:
    def __init__(self, parsed_output):
        self.messages = FakeMessages(parsed_output)


def patch_supabase(monkeypatch, module, table_data):
    fake = FakeSupabase(table_data)
    monkeypatch.setattr(module, "create_client", lambda *args, **kwargs: fake)
    return fake


def patch_claude(monkeypatch, module, parsed_output):
    monkeypatch.setattr(
        module.boto3,
        "Session",
        lambda: SimpleNamespace(region_name="us-east-1")
    )
    monkeypatch.setattr(
        module,
        "AnthropicBedrock",
        lambda aws_region=None: FakeAnthropicClient(parsed_output)
    )


# ============================================================
# 1-3 classify_ticket_v2
# ============================================================

def test_classify_ticket_v2_valid_complaint(monkeypatch):
    monkeypatch.setattr(
        classify_mod,
        "validate_safety",
        lambda text: (True, "Request passed safety check.")
    )

    classification = SimpleNamespace(
        valid=True,
        validation_reason="Valid complaint",
        category="response_time",
        urgency=7,
        sentiment="negative",
        suggested_action="Escalate the repeated lateness issue.",
        draft_reply="Old Week 8 reply."
    )

    monkeypatch.setattr(
        classify_mod,
        "classify_ticket_aws_claude",
        lambda text: classification
    )
    monkeypatch.setattr(
        classify_mod,
        "policies",
        lambda category: "Response-time issues must be acknowledged within 24 hours."
    )
    monkeypatch.setattr(
        classify_mod,
        "draft_policy_reply",
        lambda text, classification, policy: "Policy-aware customer reply."
    )

    result = classify_mod.classify_ticket_v2(
        "The guard was 50 minutes late again."
    )

    assert result.valid is True
    assert result.category == "response_time"
    assert result.urgency == 7
    assert result.sentiment == "negative"
    assert result.policy == "Response-time issues must be acknowledged within 24 hours."
    assert result.draft_reply == "Policy-aware customer reply."


def test_classify_ticket_v2_blocks_unsafe_input(monkeypatch):
    monkeypatch.setattr(
        classify_mod,
        "validate_safety",
        lambda text: (False, "Request blocked by safety guardrail.")
    )

    def should_not_run(text):
        pytest.fail("Classifier should not run after safety failure.")

    monkeypatch.setattr(
        classify_mod,
        "classify_ticket_aws_claude",
        should_not_run
    )

    result = classify_mod.classify_ticket_v2("Unsafe test input")

    assert result.valid is False
    assert "guardrail" in result.reason.lower()
    assert result.category is None
    assert result.draft_reply is None


def test_classify_ticket_v2_rejects_non_complaint(monkeypatch):
    monkeypatch.setattr(
        classify_mod,
        "validate_safety",
        lambda text: (True, "Request passed safety check.")
    )

    classification = SimpleNamespace(
        valid=False,
        validation_reason="This is a pricing inquiry, not a complaint.",
        category=None,
        urgency=None,
        sentiment=None,
        suggested_action=None,
        draft_reply=None
    )

    monkeypatch.setattr(
        classify_mod,
        "classify_ticket_aws_claude",
        lambda text: classification
    )

    result = classify_mod.classify_ticket_v2(
        "What is the price of your security service?"
    )

    assert result.valid is False
    assert "not a complaint" in result.reason.lower()
    assert result.category is None
    assert result.policy is None
    assert result.draft_reply is None


# ============================================================
# 4-6 summarize_complaint
# ============================================================

def test_get_complaint_returns_description(monkeypatch):
    complaint = {
        "id": "complaint-123",
        "description": "The invoice includes two unapproved guard shifts."
    }

    patch_supabase(
        monkeypatch,
        summary_mod,
        {"complaints": [complaint]}
    )

    result = summary_mod.get_complaint("complaint-123")

    assert result == "The invoice includes two unapproved guard shifts."


def test_get_complaint_returns_none_when_missing(monkeypatch):
    patch_supabase(
        monkeypatch,
        summary_mod,
        {"complaints": []}
    )

    result = summary_mod.get_complaint("does-not-exist")

    assert result is None


def test_summarize_complaint_returns_structured_summary(monkeypatch):
    ai_result = summary_mod.ComplaintSummary(
        valid=True,
        complaint_id=None,
        summary="Client disputes two unapproved guard shifts on the latest invoice.",
        key_issue="Unauthorized billing.",
        severity="High",
        reason="Financial discrepancy requires prompt review."
    )

    patch_claude(monkeypatch, summary_mod, ai_result)

    result = summary_mod.summarize_complaint(
        "Our invoice includes two guard shifts we never approved."
    )

    assert result.valid is True
    assert result.key_issue == "Unauthorized billing."
    assert result.severity == "High"
    assert "invoice" in result.summary.lower()


# ============================================================
# 7-9 extract_contract_data
# ============================================================

def test_get_contract_returns_single_contract(monkeypatch):
    contract = {
        "id": "contract-123",
        "name": "Scarborough East Office Tower",
        "start_date": "2026-05-29",
        "end_date": "2027-07-23",
        "monthly_value": 8500.0
    }

    patch_supabase(
        monkeypatch,
        contract_mod,
        {"contracts": [contract]}
    )

    result = contract_mod.get_contract("contract-123")

    assert result["id"] == "contract-123"
    assert result["monthly_value"] == 8500.0


def test_get_other_details_groups_contract_history(monkeypatch):
    patch_supabase(
        monkeypatch,
        contract_mod,
        {
            "surveys": [{"nps_score": 7, "satisfaction": 4}],
            "complaints": [{"description": "Guard arrived late."}],
            "incidents": [{"incident_type": "Trespassing"}]
        }
    )

    result = contract_mod.get_other_details("contract-123")

    assert len(result["surveys"]) == 1
    assert len(result["complaints"]) == 1
    assert len(result["incidents"]) == 1
    assert result["incidents"][0]["incident_type"] == "Trespassing"


def test_contract_data_returns_structured_ai_result(monkeypatch):
    ai_result = contract_mod.ContractSummaryAI(
        start_date="2026-05-29",
        end_date="2027-07-23",
        contract_value="$8,500.00 per month",
        renewal_terms="Renewal status is Not Due.",
        payment_terms="Invoice auto-creation is enabled.",
        complaints=0,
        survey="1 positive survey.",
        incident=1,
        renewal_score=7,
        renewal_score_reason="Positive survey, no complaints, one handled incident.",
        other_information="Active recurring contract."
    )

    patch_claude(monkeypatch, contract_mod, ai_result)

    contract = {
        "start_date": "2026-05-29",
        "end_date": "2027-07-23",
        "monthly_value": 8500.0
    }

    other_details = {
        "surveys": [{"nps_score": 7, "satisfaction": 4}],
        "complaints": [],
        "incidents": [{"severity": "Medium"}]
    }

    result = contract_mod.contract_data(
        contract_details=contract,
        other_details=other_details
    )

    assert result.start_date == "2026-05-29"
    assert result.complaints == 0
    assert result.incident == 1
    assert result.renewal_score == 7


# ============================================================
# 10-12 draft_followup
# ============================================================

def test_followup_get_contract_returns_none_when_missing(monkeypatch):
    patch_supabase(
        monkeypatch,
        followup_mod,
        {"contracts": []}
    )

    result = followup_mod.get_contract("missing-contract")

    assert result is None


def test_followup_get_other_details_groups_history(monkeypatch):
    patch_supabase(
        monkeypatch,
        followup_mod,
        {
            "surveys": [{"nps_score": 9, "satisfaction": 5}],
            "complaints": [],
            "incidents": [{"incident_type": "Trespassing"}]
        }
    )

    result = followup_mod.get_other_details("contract-123")

    assert len(result["surveys"]) == 1
    assert result["complaints"] == []
    assert len(result["incidents"]) == 1


def test_followup_draft_email_returns_subject_and_message(monkeypatch):
    ai_result = followup_mod.FollowupDraftAI(
        followup_type="Service Satisfaction Follow-Up",
        subject="Checking In on Your Service Experience - Scarborough East Office Tower",
        message=(
            "We wanted to check in and see how you are finding our security "
            "services. Please let us know if you have any questions or concerns."
        )
    )

    patch_claude(monkeypatch, followup_mod, ai_result)

    contract = {
        "name": "Scarborough East Office Tower",
        "status": "Active",
        "start_date": "2026-05-29"
    }

    other_details = {
        "surveys": [{"nps_score": 7, "satisfaction": 4}],
        "complaints": [],
        "incidents": []
    }

    result = followup_mod.followup_draft_email(
        contract_details=contract,
        other_details=other_details
    )

    assert result.followup_type == "Service Satisfaction Follow-Up"
    assert "Scarborough East Office Tower" in result.subject
    assert len(result.message) > 20

# ============================================================
# EXTRA EMPTY-HISTORY COVERAGE
# ============================================================

def test_summarize_complaint_missing_record_does_not_fail(monkeypatch):
    """
    summarize_complaint service:
    If Supabase has no complaint for the requested ID, get_complaint()
    should return None cleanly instead of raising an exception.
    """

    patch_supabase(
        monkeypatch,
        summary_mod,
        {"complaints": []}
    )

    result = summary_mod.get_complaint("missing-complaint-id")

    assert result is None


def test_followup_get_other_details_handles_all_empty_lists(monkeypatch):
    """
    draft_followup service:
    Contract exists, but there are no surveys, complaints, or incidents.
    The helper should still return the expected structure with empty lists.
    """

    patch_supabase(
        monkeypatch,
        followup_mod,
        {
            "surveys": [],
            "complaints": [],
            "incidents": []
        }
    )

    result = followup_mod.get_other_details("contract-123")

    assert result == {
        "surveys": [],
        "complaints": [],
        "incidents": []
    }


def test_followup_draft_email_handles_empty_history(monkeypatch):
    """
    draft_followup service:
    The LLM drafting function should still work when the related contract
    has no surveys, complaints, or incidents.
    """

    ai_result = followup_mod.FollowupDraftAI(
        followup_type="General Service Check-In",
        subject="Checking In on Your Service Experience - Scarborough East Office Tower",
        message=(
            "We wanted to check in and see how your security service has been going. "
            "Please let us know if you have any questions, concerns, or feedback."
        )
    )

    patch_claude(
        monkeypatch,
        followup_mod,
        ai_result
    )

    contract = {
        "id": "contract-123",
        "name": "Scarborough East Office Tower",
        "status": "Active",
        "start_date": "2026-05-29",
        "end_date": "2027-07-23",
        "monthly_value": 8500.0
    }

    other_details = {
        "surveys": [],
        "complaints": [],
        "incidents": []
    }

    result = followup_mod.followup_draft_email(
        contract_details=contract,
        other_details=other_details
    )

    assert result.followup_type == "General Service Check-In"
    assert "Scarborough East Office Tower" in result.subject
    assert result.message
    assert len(result.message) > 20
