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

### 1. Reflected XSS

- Severity: **High**
- Confidence: **High**
- CWE: CWE-79
- OWASP: A1:2021 - Injection
- File: xss.py
- Line: 8

**Description**

The application is directly echoing user input without proper sanitization, which can lead to XSS attacks.

**Evidence**

<h1><script>alert('XSS')</script></h1>

**Recommendation**

Sanitize and escape user inputs before rendering them in the response. Use Flask's built-in escaping functions or a templating engine like Jinja2.

**Secure Code Example**

```text
from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name')
    return f'<h1>{escape(name)}</h1>'
```

---

