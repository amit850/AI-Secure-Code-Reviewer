from rules.base_regex_rule import BaseRegexRule


class SSRFRule(BaseRegexRule):

    id = "SCR006"

    metadata = {
        "title": "Server-Side Request Forgery (SSRF)",
        "severity": "High",
        "confidence": "High",
        "cwe": "CWE-918",
        "owasp": "A10:2021",
        "description": "Possible Server-Side Request Forgery detected.",
        "recommendation": "Validate URLs using an allowlist. Never make server-side requests to user-controlled URLs without validation.",
        "secure_code": """
ALLOWED_DOMAINS = ["example.com"]

if urlparse(url).hostname in ALLOWED_DOMAINS:
    requests.get(url)
"""
    }

    patterns = [

        # Python requests
        r"requests\.get\s*\(",
        r"requests\.post\s*\(",
        r"requests\.put\s*\(",
        r"requests\.delete\s*\(",

        # urllib
        r"urllib\.request\.urlopen\s*\(",

        # Node.js
        r"axios\.get\s*\(",
        r"axios\.post\s*\(",
        r"fetch\s*\(",

        # Java
        r"new\s+URL\s*\(",
        r"HttpURLConnection",

        # Go
        r"http\.Get\s*\(",
        r"http\.Post\s*\(",
    ]