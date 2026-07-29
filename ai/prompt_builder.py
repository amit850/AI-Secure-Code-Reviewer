from ai.prompts import SYSTEM_PROMPT
from config import MAX_CODE_LENGTH


def build_messages(filename: str, code: str) -> list:
    """
    Build messages for the LLM.
    """

    code = code[:MAX_CODE_LENGTH]

    user_prompt = f"""
Review this source code.

Filename:
{filename}

Source Code:
{code}
"""

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]