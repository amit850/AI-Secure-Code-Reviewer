from rules.base_regex_rule import BaseRegexRule


class OpenRedirectRule(BaseRegexRule):

    id = "SCR011"

    metadata = {
        "title": "Open Redirect",
        "severity": "Medium",
        "confidence": "High",
        "cwe": "CWE-601",
        "owasp": "A01:2021",
        "description": "Possible Open Redirect detected.",
        "recommendation": "Do not redirect users to untrusted URLs. Use an allowlist of trusted domains.",
        "secure_code": """
ALLOWED = ["/home", "/dashboard"]

if next_url in ALLOWED:
    return redirect(next_url)
"""
    }

    patterns = [
        r"redirect\s*\(",
        r"HttpResponseRedirect\s*\(",
        r"sendRedirect\s*\(",
        r"Response\.Redirect\s*\(",
        r"res\.redirect\s*\(",
    ]