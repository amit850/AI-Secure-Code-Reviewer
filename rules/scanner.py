"""
Rule Scanner

Executes all registered security rules.
"""

from rules.registry import RULES


def run_rules(
    filename: str,
    code: str,
):
    """
    Execute all registered rules.
    """

    findings = []

    for rule in RULES:

        findings.extend(
            rule.scan(
                filename,
                code,
            )
        )

    return findings