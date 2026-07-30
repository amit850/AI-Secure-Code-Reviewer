from rules.base_regex_rule import BaseRegexRule


class JWTRule(BaseRegexRule):

    id = "SCR010"

    metadata = {
        "title": "JWT Security Issue",
        "severity": "High",
        "confidence": "Medium",
        "cwe": "CWE-347",
        "owasp": "A07:2021",
        "description": "Potential insecure JWT usage detected.",
        "recommendation": "Always verify JWT signatures and use strong algorithms such as RS256 or ES256.",
        "secure_code": """
jwt.decode(
    token,
    PUBLIC_KEY,
    algorithms=["RS256"]
)
"""
    }

    patterns = [
        r"jwt\.decode\s*\(",
        r"verify=False",
        r"algorithms\s*=\s*\[\s*[\"']none[\"']\s*\]",
        r"jsonwebtoken\.verify",
    ]