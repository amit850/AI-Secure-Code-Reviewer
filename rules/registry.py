from rules.hardcoded_secrets import HardcodedSecretsRule
from rules.sqli import SQLInjectionRule
from rules.xss import XSSRule
from rules.command_injection import CommandInjectionRule
from rules.path_traversal import PathTraversalRule
from rules.ssrf import SSRFRule
from rules.weak_hash import WeakHashRule
from rules.weak_random import WeakRandomRule
from rules.file_upload import FileUploadRule
from rules.jwt import JWTRule
from rules.open_redirect import OpenRedirectRule
from rules.xxe import XXERule

RULES = [
    HardcodedSecretsRule(),
    SQLInjectionRule(),
    XSSRule(),
    CommandInjectionRule(),
    PathTraversalRule(),
    SSRFRule(),
    WeakHashRule(),
    WeakRandomRule(),
    FileUploadRule(),
    JWTRule(),
    OpenRedirectRule(),
    XXERule(),
]