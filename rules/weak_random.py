from rules.base_regex_rule import BaseRegexRule


class WeakRandomRule(BaseRegexRule):

    id = "SCR008"

    metadata = {
        "title": "Weak Random Number Generator",
        "severity": "Medium",
        "confidence": "High",
        "cwe": "CWE-338",
        "owasp": "A02:2021",
        "description": "Weak random number generator detected.",
        "recommendation": "Use cryptographically secure random generators such as Python's secrets module.",
        "secure_code": """
import secrets

token = secrets.token_hex(32)
"""
    }

    patterns = [
        r"random\.random\s*\(",
        r"random\.randint\s*\(",
        r"random\.choice\s*\(",
        r"Math\.random\s*\(",
        r"new\s+Random\s*\(",
    ]