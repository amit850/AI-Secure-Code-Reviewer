from rules.base_regex_rule import BaseRegexRule


class FileUploadRule(BaseRegexRule):

    id = "SCR009"

    metadata = {
        "title": "Insecure File Upload",
        "severity": "High",
        "confidence": "Medium",
        "cwe": "CWE-434",
        "owasp": "A05:2021",
        "description": "Possible insecure file upload detected.",
        "recommendation": "Validate file extension, MIME type, file size, and store uploads outside the web root.",
        "secure_code": """
ALLOWED_EXTENSIONS = {"jpg", "png", "pdf"}

if extension in ALLOWED_EXTENSIONS:
    save_file(file)
"""
    }

    patterns = [
        r"request\.files",
        r"\.save\s*\(",
        r"IFormFile",
        r"MultipartFile",
        r"move_uploaded_file\s*\(",
        r"multer\s*\(",
    ]