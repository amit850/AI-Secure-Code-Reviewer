from rules.base_regex_rule import BaseRegexRule


class CommandInjectionRule(BaseRegexRule):

    id = "SCR004"

    metadata = {
        "title": "Command Injection",
        "severity": "Critical",
        "confidence": "High",
        "cwe": "CWE-78",
        "owasp": "A03:2021",
        "description": "Possible Command Injection detected.",
        "recommendation": "Avoid passing user input to OS commands. Use safe APIs or validate input.",
        "secure_code": """
import subprocess

subprocess.run(
    ["ping", hostname],
    shell=False
)
"""
    }

    patterns = [
        r"os\.system\s*\(",
        r"os\.popen\s*\(",
        r"subprocess\.Popen\s*\(",
        r"subprocess\.call\s*\(",
        r"subprocess\.run\s*\(",
        r"subprocess\.check_output\s*\(",
        r"subprocess\.check_call\s*\(",
    ]