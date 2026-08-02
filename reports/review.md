# AI Secure Code Review Report

## Summary

- Total Findings: 1
- Critical: 0
- High: 1
- Medium: 0
- Low: 0
- Info: 0

---

## Findings

### 1. Cross-Site Scripting (XSS)

- Severity: **High**
- Confidence: **Certain**
- CWE: CWE-79
- OWASP: A1: Injection
- File: xss.py
- Line: 6

**Description**

The application is vulnerable to Cross-Site Scripting because it directly outputs user-supplied input without proper sanitization or encoding.

**Evidence**

<h1>

**Recommendation**

Sanitize and escape the user input before outputting it in HTML.

**Secure Code Example**

```text
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get('name')
    return '<h1>' + escape(name) + '</h1>'
```

---

