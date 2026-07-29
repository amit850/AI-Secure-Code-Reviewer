import time

from ollama import chat

from config import LLM_MODEL, LLM_OPTIONS


def generate_response(messages):

    retries = 3

    for attempt in range(retries):

        try:

            response = chat(
                model=LLM_MODEL,
                messages=messages,
                format="json",
                options=LLM_OPTIONS,
            )

            return response["message"]["content"]

        except Exception as e:

            if attempt == retries - 1:
                raise

            print(f"[!] Ollama Error: {e}")
            print("[*] Retrying...\n")

            time.sleep(2)