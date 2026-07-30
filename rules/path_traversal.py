from rules.base_regex_rule import BaseRegexRule


class PathTraversalRule(BaseRegexRule):

    id = "SCR005"

    metadata = {
        "title": "Path Traversal",
        "severity": "High",
        "confidence": "High",
        "cwe": "CWE-22",
        "owasp": "A01:2021",
        "description": "Possible Path Traversal detected.",
        "recommendation": "Validate file paths and restrict access to expected directories.",
        "secure_code": """
from pathlib import Path

base = Path("/safe")

safe = (base / filename).resolve()
"""
    }

    patterns = [
        r"open\s*\(",
        r"FileInputStream\s*\(",
        r"FileReader\s*\(",
        r"readFileSync\s*\(",
    ]