# AI Secure Code Review Report

## Summary

- Total Findings: 2
- Critical: 0
- High: 2
- Medium: 0
- Low: 0
- Info: 0

---

## Findings

### 1. Insecure File Upload

- Severity: **High**
- Confidence: **Medium**
- CWE: CWE-434
- OWASP: A05:2021
- File: file_upload.py
- Line: 3

**Description**

Possible insecure file upload detected.

**Evidence**

request.files

**Recommendation**

Validate file extension, MIME type, file size, and store uploads outside the web root.

**Secure Code Example**

```text

ALLOWED_EXTENSIONS = {"jpg", "png", "pdf"}

if extension in ALLOWED_EXTENSIONS:
    save_file(file)

```

---

### 2. Insecure File Upload

- Severity: **High**
- Confidence: **Medium**
- CWE: CWE-434
- OWASP: A05:2021
- File: file_upload.py
- Line: 5

**Description**

Possible insecure file upload detected.

**Evidence**

.save(

**Recommendation**

Validate file extension, MIME type, file size, and store uploads outside the web root.

**Secure Code Example**

```text

ALLOWED_EXTENSIONS = {"jpg", "png", "pdf"}

if extension in ALLOWED_EXTENSIONS:
    save_file(file)

```

---

