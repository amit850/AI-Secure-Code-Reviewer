# ==========================================================
# Hybrid Security Reviewer
#
# Pipeline:
#
# Rule Engine
#        +
# AI Review
#        ↓
# Merge Findings
# ==========================================================

from copy import deepcopy

from ai.prompt_builder import build_messages
from ai.llm import generate_response
from ai.parser import parse_review

from rules.scanner import run_rules
from rules.dedup import deduplicate_findings

def review_code_ai(
    filename: str,
    code: str,
):
    """
    Execute only the AI review.
    """

    messages = build_messages(
        filename=filename,
        code=code,
    )

    response = generate_response(messages)

    return parse_review(response)


def merge_reports(
    ai_report,
    rule_findings,
):
    """
    Merge Rule Engine findings with AI findings.
    """

    report = deepcopy(ai_report)

    report.findings = deduplicate_findings(
        rule_findings,
        report.findings,
    )

    report.summary.total_findings = len(
        report.findings
    )

    severity = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "info": 0,
    }

    for finding in report.findings:

        level = finding.severity.lower()

        if level in severity:
            severity[level] += 1

    report.summary.critical = severity["critical"]
    report.summary.high = severity["high"]
    report.summary.medium = severity["medium"]
    report.summary.low = severity["low"]
    report.summary.info = severity["info"]

    return report


def review_code(
    filename: str,
    code: str,
):
    """
    Complete Hybrid Review Pipeline.
    """

    # --------------------------
    # Rule Engine
    # --------------------------

    rule_findings = run_rules(
        filename,
        code,
    )

    # --------------------------
    # AI Review
    # --------------------------

    ai_report = review_code_ai(
        filename,
        code,
    )

    # --------------------------
    # Merge
    # --------------------------

    return merge_reports(
        ai_report,
        rule_findings,
    )