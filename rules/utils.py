"""
Rule Engine Utilities

Common helper functions shared by all security rules.
"""

import re

from schemas.findings import Finding


def get_line_number(code: str, position: int) -> int:
    """
    Convert character position to line number.
    """

    return code.count("\n", 0, position) + 1


def create_finding(
    *,
    title: str,
    severity: str,
    confidence: str,
    cwe: str,
    owasp: str,
    filename: str,
    line: int,
    description: str,
    evidence: str,
    recommendation: str,
    secure_code_example: str,
) -> Finding:
    """
    Create a Finding object.
    """

    return Finding(
        title=title,
        severity=severity,
        confidence=confidence,
        cwe=cwe,
        owasp=owasp,
        file=filename,
        line=line,
        description=description,
        evidence=evidence,
        recommendation=recommendation,
        secure_code_example=secure_code_example,
    )


def find_pattern_matches(
    pattern: str,
    code: str,
):
    """
    Return regex match iterator.
    """

    return re.finditer(
        pattern,
        code,
        re.IGNORECASE | re.MULTILINE,
    )