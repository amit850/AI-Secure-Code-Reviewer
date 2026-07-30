"""
Rule Engine

Runs all static security rules.
"""

from rules.hardcoded_secrets import HardcodedSecretsRule


class RuleEngine:

    def __init__(self):

        self.rules = [

            HardcodedSecretsRule(),

        ]

    def scan(
        self,
        file_path: str,
        source_code: str
    ) -> list[dict]:

        findings = []

        for rule in self.rules:

            findings.extend(

                rule.scan(
                    file_path=file_path,
                    source_code=source_code
                )

            )

        return findings