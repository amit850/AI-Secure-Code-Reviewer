import re


def normalize_cwe(cwe: str) -> str:
    """
    Extract only the CWE ID.
    Example:
    'CWE-798: Use of Hard-coded Credentials'
    -> 'CWE-798'
    """
    match = re.search(r"CWE-\d+", cwe)
    return match.group() if match else cwe


def deduplicate_findings(rule_findings, ai_findings):
    unique = set()
    findings = []

    # Rule findings first (higher priority)
    for finding in rule_findings:
        key = (
            finding.file.lower(),
            finding.line,
            normalize_cwe(finding.cwe),
        )
        unique.add(key)
        findings.append(finding)

    # AI findings
    for finding in ai_findings:
        key = (
            finding.file.lower(),
            finding.line,
            normalize_cwe(finding.cwe),
        )

        if key not in unique:
            unique.add(key)
            findings.append(finding)

    return findings