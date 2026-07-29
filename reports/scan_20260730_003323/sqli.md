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
- Confidence: **High**
- CWE: CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- OWASP: A1:2021 - Injection
- File: sqli.py
- Line: 5

**Description**

The code is vulnerable to SQL injection because it directly concatenates user input into the SQL query without proper sanitization or parameterized queries.

**Evidence**

query = "SELECT * FROM users WHERE id = " + user_id

**Recommendation**

Use parameterized queries to prevent SQL injection. Modify the code as follows:

**Secure Code Example**

```text
import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
user_id = input("Enter ID: ")
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

---

