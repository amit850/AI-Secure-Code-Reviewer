# ==========================================================
# AI Secure Code Reviewer Configuration
# ==========================================================

# -------------------------
# LLM Configuration
# -------------------------

# Local LLM model used for security review

LLM_MODEL="qwen2.5-coder:7b"


# -------------------------
# Output Configuration
# -------------------------

# Save generated reports
REPORT_FOLDER="reports"


# -------------------------
# Supported Languages
# -------------------------

SUPPORTED_LANGUAGES=[
    ".java",
    ".py",
    ".go"
]



# -------------------------
# Review Configuration
# -------------------------

# Maximum code size (characters) sent to AI
MAX_CODE_LENGTH = 12000