from rules.base_regex_rule import BaseRegexRule


class SQLInjectionRule(BaseRegexRule):

    id = "SCR002"

    metadata = {
        "title": "SQL Injection",
        "severity": "High",
        "confidence": "High",
        "cwe": "CWE-89",
        "owasp": "A03:2021",
        "description": "Possible SQL Injection detected.",
        "recommendation": "Use parameterized queries.",
        "secure_code": """
cursor.execute(
    "SELECT * FROM users WHERE id=?",
    (user_id,)
)
"""
    }

    patterns = [
        r"SELECT.*\+",
        r"INSERT.*\+",
        r"UPDATE.*\+",
        r"DELETE.*\+",
        r'f".*SELECT.*{.*}"',
        r"f'.*SELECT.*{.*}'",
        r"SELECT.*%s.*%",
        r"SELECT.*format\(",
    ]