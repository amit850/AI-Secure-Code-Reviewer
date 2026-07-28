# ==========================================================
# Prompt Builder
# ==========================================================

from ai.prompts import SYSTEM_PROMPT


def build_messages(filename: str, code: str) -> list:
    """
    Build messages for the LLM.
    """

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"""
Review the following source code.

Return ONLY valid JSON.

Do not omit any field.

If a field is unknown, return "Unknown".

Filename:
{filename}

Source Code:
{code}
"""
        }
    ]