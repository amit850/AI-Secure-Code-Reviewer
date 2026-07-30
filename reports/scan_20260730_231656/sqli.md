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

### 1. SQL Injection

- Severity: **High**
- Confidence: **Medium**
- CWE: CWE-89
- OWASP: A03:2021
- File: sqli.py
- Line: 5

**Description**

Possible SQL Injection detected.

**Evidence**

SELECT * FROM users WHERE id = " +

**Recommendation**

Use parameterized queries instead of string concatenation.

**Secure Code Example**

```text

cursor.execute(
    "SELECT * FROM users WHERE id=?",
    (user_id,)
)

```

---

