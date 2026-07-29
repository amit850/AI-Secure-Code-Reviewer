# ==========================================================
# Folder Reader
# ==========================================================

from pathlib import Path

# Supported source code files
SUPPORTED_EXTENSIONS = (
    ".py",
    ".java",
    ".go",
)


def get_source_files(folder_path: str):
    """
    Return all supported source code files
    from a folder recursively.
    """

    files = []

    folder = Path(folder_path)

    for file in folder.rglob("*"):

        if file.is_file() and file.suffix in SUPPORTED_EXTENSIONS:
            files.append(str(file))

    return files