from rules.base_regex_rule import BaseRegexRule


class XXERule(BaseRegexRule):

    id = "SCR012"

    metadata = {
        "title": "XML External Entity (XXE)",
        "severity": "High",
        "confidence": "High",
        "cwe": "CWE-611",
        "owasp": "A05:2021",
        "description": "Possible XML External Entity processing detected.",
        "recommendation": "Disable external entity resolution in XML parsers.",
        "secure_code": """
from defusedxml import ElementTree

tree = ElementTree.parse(xml_file)
"""
    }

    patterns = [
        r"xml\.etree\.ElementTree\.parse\s*\(",
        r"lxml\.etree\.parse\s*\(",
        r"DocumentBuilderFactory",
        r"SAXParserFactory",
        r"XMLInputFactory",
        r"<!DOCTYPE",
    ]