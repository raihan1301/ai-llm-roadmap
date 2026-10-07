# Week 8 — GPT-OSS-120B vs Claude Sonnet 4.6 Complaint Classification

## Comparison Setup

The same 5 SmartOps complaints were sent to both models using the same classification schema:

- `category`
- `urgency`
- `sentiment`
- `suggested_action`
- `draft_reply`

Models compared:

- **GPT:** OpenAI GPT-OSS-120B via Amazon Bedrock
- **Claude:** Claude Sonnet 4.6 via Amazon Bedrock

The comparison focuses on category accuracy, urgency judgment, grounding, action quality, and reply quality.

---

## Summary

| # | Complaint Type | GPT Category / Urgency | Claude Category / Urgency | Winner | Reason |
|---|---|---|---|---|---|
| 1 | Repeated guard lateness | `response_time` / 7 | `response_time` / 7 | **GPT** | Both classified correctly, but GPT's reply stays more clearly in future-action language and avoids implying an escalation has already happened. |
| 2 | Guard using phone / not monitoring entrance | `staff` / 5 | `staff` / 7 | **GPT** | Claude treated the issue as more urgent, but GPT gave a more measured action plan and its reply was better grounded without claiming a formal escalation had already occurred. |
| 3 | Missed patrol checkpoints / weak reports | `service_quality` / 5 | `service_quality` / 5 | **Claude** | Both were accurate. Claude's action plan was more focused on the exact operational problem: logs, checkpoints, reporting standards, and follow-up verification. |
| 4 | Unauthorized access to restricted area | `incident` / 9 | `incident` / 9 | **Claude** | Claude remained grounded and thorough. GPT incorrectly stated that an investigation had already been launched and invented a deadline for a preliminary report. |
| 5 | Unapproved guard shifts on invoice | `billing` / 5 | `billing` / 4 | **Claude** | Claude handled the billing discrepancy cautiously and avoided inventing a response deadline. GPT promised a follow-up by the next business day even though no SLA was provided. |

---

## Complaint 1 — Repeated Guard Lateness

**Complaint**

> The security guard scheduled for the evening shift arrived 50 minutes late. This is the third late arrival at this site in the past two weeks, and our front desk was left without coverage during that time.

### GPT-OSS-120B

- **Category:** `response_time`
- **Urgency:** 7
- **Sentiment:** `negative`
- **Suggested action:** Investigate the repeated lateness, review scheduling, add backup coverage, speak with the guard, monitor attendance, and communicate corrective steps to the client.

### Claude Sonnet 4.6

- **Category:** `response_time`
- **Urgency:** 7
- **Sentiment:** `negative`
- **Suggested action:** Escalate to the site supervisor and operations manager, investigate root cause and attendance history, implement corrective action, and consider relief coverage.

### Winner: GPT

Both models agreed on the classification and urgency. GPT was slightly better grounded in the client reply because it framed the next steps as future actions. Claude's draft said the issue was already being escalated internally, which was not established by the complaint.

---

## Complaint 2 — Guard Not Monitoring Entrance

**Complaint**

> The guard on duty was repeatedly using his phone and was not monitoring the main entrance. Our site manager spoke to him twice during the shift, but the behavior continued.

### GPT-OSS-120B

- **Category:** `staff`
- **Urgency:** 5
- **Sentiment:** `negative`
- **Suggested action:** Investigate the conduct, gather details, meet with the guard, document the issue, consider discipline if it continues, and monitor performance.

### Claude Sonnet 4.6

- **Category:** `staff`
- **Urgency:** 7
- **Sentiment:** `negative`
- **Suggested action:** Escalate to operations, review the guard's conduct history, start a disciplinary review, consider reassignment, and follow up with the site manager.

### Winner: GPT

Claude reasonably treated the unattended entrance as more urgent, but GPT's response was more measured and better grounded. Claude's draft again implied that a formal escalation was already underway.

---

## Complaint 3 — Missed Checkpoints and Weak Reporting

**Complaint**

> The overnight security service has been inconsistent this week. Patrol rounds are being completed, but several required checkpoints are being missed and the daily reports do not include enough detail.

### GPT-OSS-120B

- **Category:** `service_quality`
- **Urgency:** 5
- **Sentiment:** `negative`
- **Suggested action:** Review patrol logs, reinforce procedures, monitor future patrols, improve reporting, and keep the client updated.

### Claude Sonnet 4.6

- **Category:** `service_quality`
- **Urgency:** 5
- **Sentiment:** `negative`
- **Suggested action:** Review patrol logs and reports, identify missed checkpoints, reinforce checkpoint/reporting standards, and perform a follow-up review.

### Winner: Claude

Both models were accurate, but Claude's response stayed tightly focused on the exact operational problem and proposed a clearer verification step after corrective action.

---

## Complaint 4 — Unauthorized Access to Restricted Area

**Complaint**

> An unauthorized person entered the restricted storage area after following an employee through the access-controlled door. The guard noticed the individual several minutes later and escorted them out. We need this reviewed immediately.

### GPT-OSS-120B

- **Category:** `incident`
- **Urgency:** 9
- **Sentiment:** `negative`
- **Suggested action:** Review access logs and CCTV, interview involved people, investigate the access-control failure, and report findings.

### Claude Sonnet 4.6

- **Category:** `incident`
- **Urgency:** 9
- **Sentiment:** `negative`
- **Suggested action:** Escalate the incident, review access-control logs and CCTV, interview involved personnel, assess possible compromise, and reinforce tailgating procedures.

### Winner: Claude

Claude was more complete and remained grounded. GPT's draft incorrectly said an investigation had already been launched and promised a preliminary report within a few hours, neither of which was provided in the complaint.

---

## Complaint 5 — Unapproved Charges on Invoice

**Complaint**

> Our latest invoice includes charges for two additional guard shifts that were not scheduled or approved by our team. Please review the invoice and explain why these hours were billed.

### GPT-OSS-120B

- **Category:** `billing`
- **Urgency:** 5
- **Sentiment:** `negative`
- **Suggested action:** Review invoice details, compare against shift logs, identify whether the charges were authorized or erroneous, and correct the invoice if needed.

### Claude Sonnet 4.6

- **Category:** `billing`
- **Urgency:** 4
- **Sentiment:** `negative`
- **Suggested action:** Cross-check the invoice against approved schedules and deployment records, determine the source of the discrepancy, explain the findings, and correct the invoice if necessary.

### Winner: Claude

Both models handled the billing issue correctly. Claude was more cautious and avoided inventing a deadline. GPT promised a follow-up by the end of the next business day even though no response SLA was supplied.

---

## Overall Result

- **GPT-OSS-120B wins:** 2 / 5
- **Claude Sonnet 4.6 wins:** 3 / 5

### Key Findings

Both models produced the correct category and sentiment across all five complaints. The largest differences were in **urgency scoring**, **how aggressive the recommended actions were**, and **whether the draft reply introduced unsupported operational claims**.

Claude generally produced stronger operational reasoning, especially for service-quality, security-incident, and billing complaints. GPT performed well on the first two complaints and tended to produce detailed action plans, but it occasionally invented commitments such as investigation status or response deadlines.

The experiment also shows an important Structured Outputs lesson: enforcing a schema guarantees the **shape of the response**, but it does not guarantee identical judgment, factual grounding, or business-policy decisions across models.

---

## Recommendation for SmartOps

For a production classifier, the category definitions and urgency rubric should be explicitly defined in the system prompt so different models interpret complaints consistently.

Draft replies should also follow a grounding rule:

> Never claim that an action has already been taken, or promise a deadline, unless that information is present in SmartOps data or explicitly provided in the complaint.

