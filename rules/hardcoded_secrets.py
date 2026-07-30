"""
Hardcoded Secret Detection Rule
"""

from rules.base import BaseRule
from rules.utils import (
    create_finding,
    find_pattern_matches,
    get_line_number,
)


class HardcodedSecretsRule(BaseRule):

    id = "SCR001"
    name = "Hardcoded Secrets"
    description = "Detect hardcoded secrets."

    PATTERN = (
        r"(password|passwd|pwd|secret|"
        r"api[_-]?key|apikey|"
        r"token|access[_-]?token|"
        r"client[_-]?secret)"
        r"\s*[:=]\s*[\"'][^\"']+[\"']"
    )

    def scan(
        self,
        filename: str,
        code: str,
    ):

        findings = []

        for match in find_pattern_matches(
            self.PATTERN,
            code,
        ):

            findings.append(
                create_finding(
                    title=self.name,
                    severity="High",
                    confidence="High",
                    cwe="CWE-798",
                    owasp="A02:2021",
                    filename=filename,
                    line=get_line_number(
                        code,
                        match.start(),
                    ),
                    description="Hardcoded secret detected.",
                    evidence=match.group(),
                    recommendation=(
                        "Store secrets in environment variables "
                        "or a secret manager."
                    ),
                    secure_code_example="""
import os

password = os.getenv("DB_PASSWORD")
""",
                )
            )

        return findings