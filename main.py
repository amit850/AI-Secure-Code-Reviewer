# ==========================================================
# AI Secure Code Reviewer
# Entry Point
#
# Purpose:
# - Accept a file or folder from the command line.
# - If it's a file -> Review that file.
# - If it's a folder -> Review every supported source file.
# ==========================================================

import os
import sys

from utils.report_manager import create_scan_directory
from utils.file_reader import read_code_file
from utils.folder_reader import get_source_files

from ai.reviewer import review_code

from reports.manager import (
    generate_reports,
    generate_scan_reports,
)

from reports.summary import (
    generate_summary,
    save_summary,
)


def main():
    """
    Main entry point of the application.
    """

    # ------------------------------------------------------
    # Check whether user provided a path
    # Example:
    # python main.py test_cases
    # python main.py test_cases/sqli.py
    # ------------------------------------------------------
    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py <source_code_file_or_folder>")
        return

    # Read path from command line
    path = sys.argv[1]

    # ------------------------------------------------------
    # CASE 1 : User provided a single source code file
    # ------------------------------------------------------
    if os.path.isfile(path):

        print("[+] Reading source code...")

        filename, code = read_code_file(path)

        print("[+] Reviewing code with AI...")

        report = review_code(
            filename=filename,
            code=code,
        )

        print("[+] Generating report...")

        output_dir = create_scan_directory("reports")

        generate_reports(
            filename=filename,
            report=report,
            output_dir=output_dir,
        )

        print("\n===================================")
        print(" Review Completed Successfully")
        print("===================================")
        print(f"Reports saved to: {output_dir}")

    # ------------------------------------------------------
    # CASE 2 : User provided a folder
    # ------------------------------------------------------
    elif os.path.isdir(path):

        print("[+] Searching source files...")

        files = get_source_files(path)

        if not files:
            print("No supported source code files found.")
            return

        print(f"[+] Found {len(files)} file(s).\n")

        scan_directory = create_scan_directory("reports")

        scan_reports = []

        # Scan every file
        for file in files:

            print(f"[+] Scanning: {file}")

            filename, code = read_code_file(file)

            report = review_code(
                filename=filename,
                code=code,
            )

            scan_reports.append(
                (
                    filename,
                    report,
                )
            )

            generate_reports(
                filename=filename,
                report=report,
                output_dir=scan_directory,
            )

            print(f"[✓] Completed: {filename}\n")

        # --------------------------------------------------
        # Generate Summary Report
        # --------------------------------------------------
        summary = generate_summary(scan_reports)

        save_summary(
            summary,
            scan_directory,
        )

        # --------------------------------------------------
        # Generate SARIF Report
        # --------------------------------------------------
        generate_scan_reports(
            reports=scan_reports,
            output_dir=scan_directory,
        )

        print("===================================")
        print(" Folder Scan Completed")
        print("===================================")
        print(f"Reports saved to: {scan_directory}")

    # ------------------------------------------------------
    # CASE 3 : Invalid path
    # ------------------------------------------------------
    else:
        print("Invalid file or folder path.")


# ==========================================================
# Program Entry
# ==========================================================
if __name__ == "__main__":
    main()