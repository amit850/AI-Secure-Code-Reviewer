from rules.hardcoded_secrets import HardcodedSecretsRule
from rules.sqli import SQLInjectionRule
from rules.xss import XSSRule

RULES = [
    HardcodedSecretsRule(),
    SQLInjectionRule(),
    XSSRule(),
]