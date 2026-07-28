from pathlib import Path
from config import *


def read_code_file(file_path: str) -> tuple[str, str]:
    """
    Read a source code file and return
    (filename, file_content).
    """

    path = Path(file_path)

    # Check if file exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check supported extension
    if path.suffix not in SUPPORTED_LANGUAGES:
        raise ValueError(
            f"Unsupported file type: {path.suffix}"
        )

    # Read file
    content = path.read_text(
        encoding="utf-8"
    )

    return path.name, content