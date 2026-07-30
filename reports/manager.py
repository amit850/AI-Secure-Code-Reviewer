"""
Report Manager

Responsible for generating and saving
all supported report formats.
"""

from pathlib import Path

from schemas.findings import ReviewReport

from reports.markdown import (
    generate_markdown,
    save_markdown,
)
from reports.sarif import (
    generate_sarif,
    save_sarif,
)


def generate_reports(
    filename: str,
    report: ReviewReport,
    output_dir: Path,
) -> None:
    """
    Generate and save all reports
    for a single source file.
    """

    # -------------------------
    # Markdown Report
    # -------------------------

    markdown = generate_markdown(report)

    report_name = Path(filename).stem + ".md"

    save_markdown(
        markdown=markdown,
        filename=report_name,
        output_dir=output_dir,
    )

    # -------------------------
    # Future Reports
    # -------------------------

    # save_json(...)
    # save_html(...)
    # save_sarif(...)
    def generate_scan_reports(
    reports: list[tuple[str, ReviewReport]],
    output_dir: Path,
) -> None:
    """
    Generate reports for the complete scan.
    """

    # -------------------------
    # SARIF
    # -------------------------

    sarif = generate_sarif(reports)

    save_sarif(
        sarif=sarif,
        output_dir=output_dir,
    )

    # -------------------------
    # Future
    # -------------------------

    # save_json(...)
    # save_html(...)