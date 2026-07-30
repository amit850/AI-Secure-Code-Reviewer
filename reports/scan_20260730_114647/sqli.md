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
- Confidence: **Certain**
- CWE: CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- OWASP: A1:2021 - Injection
- File: sqli.py
- Line: 5

**Description**

The user input is directly concatenated into the SQL query, which allows for SQL injection attacks.

**Evidence**

query = "SELECT * FROM users WHERE id = " + user_id

**Recommendation**

Use parameterized queries to prevent SQL injection. Replace the vulnerable line with: `cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))`

**Secure Code Example**

```text
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

---

