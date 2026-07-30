"""
Base class for Regex based rules.
"""

from rules.base import BaseRule
from rules.utils import (
    create_finding,
    find_pattern_matches,
    get_line_number,
)


class BaseRegexRule(BaseRule):

    metadata = {}
    patterns = []

    def scan(self, filename: str, code: str):

        findings = []

        for pattern in self.patterns:

            for match in find_pattern_matches(pattern, code):

                findings.append(
                    create_finding(
                        title=self.metadata["title"],
                        severity=self.metadata["severity"],
                        confidence=self.metadata["confidence"],
                        cwe=self.metadata["cwe"],
                        owasp=self.metadata["owasp"],
                        filename=filename,
                        line=get_line_number(code, match.start()),
                        description=self.metadata["description"],
                        evidence=match.group(),
                        recommendation=self.metadata["recommendation"],
                        secure_code_example=self.metadata["secure_code"],
                    )
                )

        return findings