"""
Security Mapping Utilities

Contains helper functions that convert
security taxonomy into standardized values.
"""

from data.cwe_owasp_mapping import CWE_TO_OWASP


def map_cwe_to_owasp(cwe: str) -> str:
    """
    Convert a CWE value returned by the LLM
    into a standardized OWASP category.

    Supports inputs like:

    CWE-89
    CWE-89: SQL Injection
    cwe-89
    """

    if not cwe:
        return "Unknown"

    cwe = cwe.strip()

    cwe_id = cwe.split(":")[0].strip().upper()

    return CWE_TO_OWASP.get(
        cwe_id,
        "Unknown"
    )