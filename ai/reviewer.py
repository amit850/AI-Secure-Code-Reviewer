# ==========================================================
# AI Security Reviewer
# ==========================================================

from ai.prompt_builder import build_messages
from ai.llm import generate_response
from ai.parser import parse_review


def review_code(filename: str, code: str):
    """
    Review source code using the LLM.
    """

    # Build LLM messages
    messages = build_messages(
        filename=filename,
        code=code
    )

    # Get AI response
    response = generate_response(messages)

    # TEMP DEBUG
    print("\n" + "=" * 80)
    print("RAW LLM RESPONSE")
    print("=" * 80)
    print(response)
    print("=" * 80 + "\n")

    # Parse + Normalize + Validate
    return parse_review(response)