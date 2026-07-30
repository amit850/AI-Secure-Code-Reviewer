"""
Rule Registry
"""

from rules.hardcoded_secrets import HardcodedSecretsRule


RULES = [
    HardcodedSecretsRule(),
]