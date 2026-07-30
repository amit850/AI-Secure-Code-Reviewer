from rules.base_regex_rule import BaseRegexRule


class HardcodedSecretsRule(BaseRegexRule):

    id = "SCR001"

    metadata = {
        "title": "Hardcoded Secrets",
        "severity": "High",
        "confidence": "High",
        "cwe": "CWE-798",
        "owasp": "A02:2021",
        "description": "Hardcoded secret detected.",
        "recommendation": "Store secrets in environment variables or a secret manager.",
        "secure_code": """
import os

password = os.getenv("DB_PASSWORD")
"""
    }

    patterns = [
        r"(password|passwd|pwd|secret|api[_-]?key|apikey|token|access[_-]?token|client[_-]?secret)\s*[:=]\s*[\"'][^\"']+[\"']"
    ]