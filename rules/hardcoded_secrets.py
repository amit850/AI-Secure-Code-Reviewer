"""
Hardcoded Secret Detection Rule
"""

import re

from rules.base import Rule


class HardcodedSecretsRule(Rule):
    """
    Detects hardcoded secrets such as:

    API_KEY
    SECRET
    PASSWORD
    TOKEN
    PRIVATE_KEY
    """

    SECRET_PATTERNS = [

        r'(?i)(api[_-]?key)\s*=\s*["\'].*?["\']',
        r'(?i)(secret)\s*=\s*["\'].*?["\']',
        r'(?i)(password)\s*=\s*["\'].*?["\']',
        r'(?i)(token)\s*=\s*["\'].*?["\']',
        r'(?i)(private[_-]?key)\s*=\s*["\'].*?["\']',

    ]

    def scan(
        self,
        file_path: str,
        source_code: str
    ) -> list[dict]:

        findings = []

        lines = source_code.splitlines()

        for line_number, line in enumerate(lines, start=1):

            for pattern in self.SECRET_PATTERNS:

                if re.search(pattern, line):

                    findings.append({

                        "title": "Hardcoded Secret",

                        "severity": "High",

                        "confidence": "Certain",

                        "cwe": "CWE-798",

                        "owasp": "Unknown",

                        "file": file_path,

                        "line": line_number,

                        "description": (
                            "Hardcoded credentials or secrets "
                            "were found in source code."
                        ),

                        "evidence": line.strip(),

                        "recommendation": (
                            "Store secrets in environment variables "
                            "or a secure secrets manager."
                        ),

                        "secure_code_example": (
                            'import os\n'
                            'API_KEY = os.getenv("API_KEY")'
                        )

                    })

                    break

        return findings