# 🔐 AI Secure Code Reviewer

AI Secure Code Reviewer is an AI-powered Static Application Security Testing (SAST) tool that reviews source code using Large Language Models (LLMs) and detects security vulnerabilities based on OWASP Top 10, CWE, and secure coding best practices.

---

# ✨ Features

- AI Powered Secure Code Review
- OWASP Top 10 Detection
- CWE Mapping
- Severity Classification
- Confidence Score
- Secure Code Recommendations
- Rule-Based Detection Engine
- Markdown Report
- HTML Dashboard
- JSON Report
- SARIF Export
- Ollama Local LLM Support
- Pydantic Validation

---

# Supported Languages

- Python
- Java
- Go

(More languages coming soon.)

---

# Detection Rules

| Rule | Description |
|------|-------------|
| SCR001 | Hardcoded Secrets |
| SCR002 | SQL Injection |
| SCR003 | Cross Site Scripting (XSS) |
| SCR004 | Command Injection |
| SCR005 | Path Traversal |
| SCR006 | SSRF |
| SCR007 | Weak Hash Algorithm |
| SCR008 | Weak Random Generator |
| SCR009 | Insecure File Upload |
| SCR010 | JWT Issues |
| SCR011 | Open Redirect |
| SCR012 | XXE |

---

# Project Structure

```
AI-Secure-Code-Reviewer/

ai/
reports/
rules/
schemas/
utils/

main.py
requirements.txt
README.md
```

---

# Installation

Clone repository

```bash
git clone https://github.com/yourusername/AI-Secure-Code-Reviewer.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

```bash
ollama pull qwen2.5-coder:7b
```

Run

```bash
python main.py
```

---

# Reports

After scanning, reports are generated inside:

```
reports/output/
```

Generated formats

- HTML
- Markdown
- JSON
- SARIF

---

# Sample Output

```
reports/output/

report.html
report.md
report.json
report.sarif
```

---

# Technologies

- Python
- Ollama
- Pydantic
- HTML
- JSON
- SARIF

---

# Roadmap

- GitHub Integration
- Pull Request Review
- Multi-language Support
- CI/CD Integration
- VS Code Extension
- SonarQube Plugin
- Custom Rule Engine

---

# License

MIT License

---

# Author

Amit Singh

Application Security Engineer