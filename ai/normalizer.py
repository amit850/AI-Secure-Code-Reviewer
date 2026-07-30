# ==========================================================
# AI Response Normalizer
# ==========================================================

from copy import deepcopy
from utils.security_mapper import map_cwe_to_owasp

# ----------------------------------------------------------
# Default Finding Template
# ----------------------------------------------------------

FINDING_TEMPLATE = {
    "title": "Unknown",
    "severity": "Unknown",
    "confidence": "Unknown",
    "cwe": "Unknown",
    "owasp": "Unknown",
    "file": "Unknown",
    "line": 0,
    "description": "",
    "evidence": "",
    "recommendation": "",
    "secure_code_example": ""
}


def normalize_response(data: dict) -> dict:
    """
    Normalize the LLM response into the expected schema.

    This function:
    1. Fixes malformed summary returned by the LLM.
    2. Normalizes finding fields.
    3. Returns data compatible with Pydantic models.
    """

    # ------------------------------------------------------
    # Fix summary if model returns a string instead of object
    # ------------------------------------------------------

    if isinstance(data.get("summary"), str):

        findings_list = data.get("findings", [])

        summary = {
            "total_findings": len(findings_list),
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }

        for finding in findings_list:

            severity = finding.get("severity", "").lower()

            if severity == "critical":
                summary["critical"] += 1

            elif severity == "high":
                summary["high"] += 1

            elif severity == "medium":
                summary["medium"] += 1

            elif severity == "low":
                summary["low"] += 1

            elif severity == "info":
                summary["info"] += 1

        data["summary"] = summary

    # ------------------------------------------------------
    # If summary is missing completely
    # ------------------------------------------------------

    elif "summary" not in data:

        data["summary"] = {
            "total_findings": 0,
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }

    # ------------------------------------------------------
    # Normalize findings
    # ------------------------------------------------------

    findings = []

    for item in data.get("findings", []):

        finding = deepcopy(FINDING_TEMPLATE)

        finding["title"] = (
            item.get("title")
            or item.get("type")
            or "Unknown"
        )

        finding["severity"] = item.get(
            "severity",
            "Unknown"
        )

        finding["confidence"] = item.get(
            "confidence",
            "Unknown"
        )

        finding["cwe"] = item.get(
            "cwe",
            "Unknown"
        )

        finding["owasp"] = map_cwe_to_owasp(
            finding["cwe"]

        )

        finding["file"] = item.get(
            "file",
            "Unknown"
        )

        finding["line"] = item.get(
            "line",
            0
        )

        finding["description"] = item.get(
            "description",
            ""
        )

        finding["evidence"] = item.get(
            "evidence",
            ""
        )

        finding["recommendation"] = item.get(
            "recommendation",
            ""
        )

        finding["secure_code_example"] = item.get(
            "secure_code_example",
            ""
        )

        findings.append(finding)

    data["findings"] = findings

    return data