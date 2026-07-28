# ==========================================================
# Security Review Schemas
# ==========================================================

from typing import List
from pydantic import BaseModel


class Finding(BaseModel):
    """
    Represents a single security finding.
    """

    title: str
    severity: str
    confidence: str
    cwe: str
    owasp: str
    file: str
    line: int
    description: str
    evidence: str
    recommendation: str
    secure_code_example: str


class Summary(BaseModel):
    """
    Summary of the security review.
    """

    total_findings: int
    critical: int
    high: int
    medium: int
    low: int
    info: int


class ReviewReport(BaseModel):
    """
    Complete security review report.
    """

    summary: Summary
    findings: List[Finding]