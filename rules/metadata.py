"""
Rule Metadata Model
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RuleMetadata:
    id: str
    title: str
    severity: str
    confidence: str
    cwe: str
    owasp: str
    description: str
    recommendation: str
    secure_code: str