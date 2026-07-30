CWE_TO_OWASP = {
    # --- A01:2025 - Broken Access Control ---
    "CWE-22": "OWASP A01:2025 - Broken Access Control",            # Path Traversal
    "CWE-352": "OWASP A01:2025 - Broken Access Control",           # CSRF
    "CWE-601": "OWASP A01:2025 - Broken Access Control",           # Open Redirect
    "CWE-918": "OWASP A01:2025 - Broken Access Control",           # SSRF (absorbed in 2025)
    "CWE-639": "OWASP A01:2025 - Broken Access Control",           # Insecure Direct Object Reference (IDOR)
    "CWE-200": "OWASP A01:2025 - Broken Access Control",           # Exposure of Sensitive Info

    # --- A02:2025 - Security Misconfiguration ---
    "CWE-16": "OWASP A02:2025 - Security Misconfiguration",         # Configuration
    "CWE-611": "OWASP A02:2025 - Security Misconfiguration",        # XXE (XML External Entity)
    "CWE-489": "OWASP A02:2025 - Security Misconfiguration",        # Active Debug Code
    "CWE-1004": "OWASP A02:2025 - Security Misconfiguration",       # Sensitive Cookie Without HttpOnly

    # --- A03:2025 - Software Supply Chain Failures (NEW) ---
    "CWE-1395": "OWASP A03:2025 - Software Supply Chain Failures", # Dependency on Vulnerable Component
    "CWE-829": "OWASP A03:2025 - Software Supply Chain Failures",  # Inclusion of Functionality from Untrusted Sphere

    # --- A04:2025 - Cryptographic Failures ---
    "CWE-327": "OWASP A04:2025 - Cryptographic Failures",          # Broken/Risky Crypto Algorithm
    "CWE-330": "OWASP A04:2025 - Cryptographic Failures",          # Insufficiently Random Values
    "CWE-311": "OWASP A04:2025 - Cryptographic Failures",          # Missing Encryption of Sensitive Data
    "CWE-326": "OWASP A04:2025 - Cryptographic Failures",          # Inadequate Encryption Strength

    # --- A05:2025 - Injection ---
    "CWE-79": "OWASP A05:2025 - Injection",                        # XSS
    "CWE-89": "OWASP A05:2025 - Injection",                        # SQL Injection
    "CWE-78": "OWASP A05:2025 - Injection",                        # OS Command Injection
    "CWE-94": "OWASP A05:2025 - Injection",                        # Code Injection

    # --- A06:2025 - Insecure Design ---
    "CWE-209": "OWASP A06:2025 - Insecure Design",                 # Information Exposure Through Error Message
    "CWE-501": "OWASP A06:2025 - Insecure Design",                 # Trust Boundary Violation

    # --- A07:2025 - Authentication Failures ---
    "CWE-259": "OWASP A07:2025 - Authentication Failures",         # Hard-coded Password
    "CWE-798": "OWASP A07:2025 - Authentication Failures",         # Hard-coded Credentials
    "CWE-287": "OWASP A07:2025 - Authentication Failures",         # Improper Authentication
    "CWE-307": "OWASP A07:2025 - Authentication Failures",         # Improper Restriction of Excessive Authentication Attempts

    # --- A08:2025 - Software or Data Integrity Failures ---
    "CWE-502": "OWASP A08:2025 - Software or Data Integrity Failures", # Deserialization of Untrusted Data
    "CWE-345": "OWASP A08:2025 - Software or Data Integrity Failures", # Insufficient Verification of Data Authenticity

    # --- A09:2025 - Security Logging and Alerting Failures ---
    "CWE-778": "OWASP A09:2025 - Security Logging and Alerting Failures", # Insufficient Logging
    "CWE-117": "OWASP A09:2025 - Security Logging and Alerting Failures", # Improper Output Neutralization for Logs

    # --- A10:2025 - Mishandling of Exceptional Conditions (NEW) ---
    "CWE-209": "OWASP A10:2025 - Mishandling of Exceptional Conditions", # Verbose Error Messages
    "CWE-476": "OWASP A10:2025 - Mishandling of Exceptional Conditions", # NULL Pointer Dereference / Uncaught Exception
    "CWE-636": "OWASP A10:2025 - Mishandling of Exceptional Conditions", # Not Failing Securely
}