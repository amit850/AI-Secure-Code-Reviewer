from rules.base_regex_rule import BaseRegexRule


class WeakHashRule(BaseRegexRule):

    id = "SCR007"

    metadata = {
        "title": "Weak Cryptographic Hash",
        "severity": "Medium",
        "confidence": "High",
        "cwe": "CWE-328",
        "owasp": "A02:2021",
        "description": "Weak cryptographic hash algorithm detected.",
        "recommendation": "Use SHA-256, SHA-384 or SHA-512 instead of MD5 or SHA1.",
        "secure_code": """
import hashlib

hashlib.sha256(data.encode()).hexdigest()
"""
    }

    patterns = [
        r"hashlib\.md5\s*\(",
        r"hashlib\.sha1\s*\(",
        r"MessageDigest\.getInstance\s*\(\s*[\"']MD5[\"']\s*\)",
        r"MessageDigest\.getInstance\s*\(\s*[\"']SHA-1[\"']\s*\)",
        r"CryptoJS\.MD5\s*\(",
        r"CryptoJS\.SHA1\s*\(",
    ]