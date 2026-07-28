# ==========================================================
# AI Response Normalizer
# ==========================================================

from copy import deepcopy


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
    Normalize LLM response into the expected schema.
    """

    findings = []

    for item in data.get("findings", []):

        finding = deepcopy(FINDING_TEMPLATE)

        # Different models may use different keys
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

        finding["owasp"] = item.get(
            "owasp",
            "Unknown"
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