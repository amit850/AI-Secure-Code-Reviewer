"""
Hardcoded Secrets Detection Rule

Detects:
- Passwords
- API Keys
- Tokens
- Secrets
- Client Secrets
"""

import re

from rules.base import BaseRule
from rules.utils import (
    create_finding,
    find_pattern_matches,
    get_line_number,
)


class HardcodedSecretsRule(BaseRule):
    """
    Detect hardcoded secrets in source code.
    """

    id = "SCR001"
    name = "Hardcoded Secrets"
    description = "Detects hardcoded credentials and secrets."

    CWE = "CWE-798"
    OWASP = "A02:2021"

    SEVERITY = "High"
    CONFIDENCE = "High"

    PATTERN = (
        r"(password|passwd|pwd|secret|api[_-]?key|apikey|"
        r"access[_-]?token|token|client[_-]?secret|"
        r"aws[_-]?secret|private[_-]?key)"
        r"\s*[:=]\s*['\"][^'\"]+['\"]"
    )

    def scan(
        self,
        filename: str,
        code: str,
    ):

        findings = []

        matches = find_pattern_matches(
            self.PATTERN,
            code,
        )

        for match in matches:

            evidence = match.group()

            line = get_line_number(
                code,
                match.start(),
            )

            findings.append(
                create_finding(
                    title=self.name,
                    severity=self.SEVERITY,
                    confidence=self.CONFIDENCE,
                    cwe=self.CWE,
                    owasp=self.OWASP,
                    filename=filename,
                    line=line,
                    description=(
                        "Hardcoded credentials detected. "
                        "Secrets should never be stored "
                        "directly in source code."
                    ),
                    evidence=evidence,
                    recommendation=(
                        "Store secrets in environment variables "
                        "or a secure secret manager."
                    ),
                    secure_code_example="""
import os

password = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")
""",
                )
            )

        return findings