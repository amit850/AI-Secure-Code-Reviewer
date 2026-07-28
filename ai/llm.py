# ==========================================================
# LLM Connection
# ==========================================================

# Import Ollama chat function

from ollama import chat

# Import model name from config
from config import LLM_MODEL




def generate_response(messages):
    """
    Send messages to the LLM and return the AI response.
    """

    response=chat(
        # Model to use
        model=LLM_MODEL,

         # Conversation messages
        messages=messages,
        format="json"
    )
    return response["message"]["content"]