# ==========================================================
# AI Secure Code Reviewer Configuration
# ==========================================================

# -------------------------
# LLM Configuration
# -------------------------

LLM_MODEL = "qwen2.5-coder:7b"

# LLM Generation Options
LLM_OPTIONS = {
    "temperature": 0,
    "num_predict": 400,
    "num_ctx": 2048,
}

# -------------------------
# Output Configuration
# -------------------------

REPORT_FOLDER = "reports"

# -------------------------
# Supported Languages
# -------------------------

SUPPORTED_LANGUAGES = [
    ".java",
    ".py",
    ".go",
]

# -------------------------
# Review Configuration
# -------------------------

MAX_CODE_LENGTH = 12000