# AI Secure Code Review Report

## Summary

- Total Findings: 1
- Critical: 1
- High: 0
- Medium: 0
- Low: 0
- Info: 0

---

## Findings

### 1. SQL Injection

- Severity: **Critical**
- Confidence: **High**
- CWE: CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- OWASP: A1:2021 - Injection
- File: sqli.py
- Line: 5

**Description**

The code is vulnerable to SQL injection because it constructs a SQL query using user input without proper sanitization.

**Evidence**

query = "SELECT * FROM users WHERE id = " + user_id

**Recommendation**

Use parameterized queries or prepared statements to prevent SQL injection.

**Secure Code Example**

```text
query = "SELECT * FROM users WHERE id = ?" cursor.execute(query, (user_id,))
```

---

