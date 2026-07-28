# ==========================================================
# AI Secure Code Reviewer
# Entry Point
# ==========================================================

import sys

from utils.file_reader import read_code_file
from ai.reviewer import review_code
from reports.markdown import (
    generate_markdown,
    save_markdown
)


def main():

    # Check command line arguments
    if len(sys.argv) != 2:

        print("Usage:")
        print("python main.py <source_code_file>")
        return

    file_path = sys.argv[1]

    print("[+] Reading source code...")

    filename, code = read_code_file(file_path)

    print("[+] Reviewing code with AI...")

    report = review_code(
        filename=filename,
        code=code
    )

    print("[+] Generating report...")

    markdown = generate_markdown(report)

    output = save_markdown(markdown)

    print()

    print("===================================")
    print(" Review Completed Successfully")
    print("===================================")

    print(f"Report saved to: {output}")


if __name__ == "__main__":
    main()