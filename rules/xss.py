from rules.base_regex_rule import BaseRegexRule


class XSSRule(BaseRegexRule):

    id = "SCR003"

    metadata = {
        "title": "Cross-Site Scripting (XSS)",
        "severity": "High",
        "confidence": "High",
        "cwe": "CWE-79",
        "owasp": "A03:2021",
        "description": "Possible Cross-Site Scripting detected.",
        "recommendation": "Escape or sanitize untrusted user input before rendering.",
        "secure_code": """
from markupsafe import escape

name = escape(user_input)
"""
    }

    patterns = [
        r"innerHTML\s*=",
        r"document\.write\s*\(",
        r"response\.write\s*\(",
        r"render_template_string\s*\(",
    ]