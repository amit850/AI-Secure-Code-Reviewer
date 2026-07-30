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

from reports.json import (
    save_json,
    save_scan_json,
)

from reports.sarif import (
    generate_sarif,
    save_sarif,
)

from reports.html import generate_html_report


def generate_reports(
    filename: str,
    report: ReviewReport,
    output_dir: Path,
) -> None:

    markdown = generate_markdown(report)

    report_name = Path(filename).stem + ".md"

    save_markdown(
        markdown=markdown,
        filename=report_name,
        output_dir=output_dir,
    )

    json_name = Path(filename).stem + ".json"

    save_json(
        report=report,
        filename=json_name,
        output_dir=output_dir,
    )
    


def generate_scan_reports(
    reports: list[tuple[str, ReviewReport]],
    output_dir: Path,
) -> None:
    """
    Generate reports for the complete scan.
    """

    # -------------------------
    # SARIF Report
    # -------------------------

    sarif = generate_sarif(reports)

    save_sarif(
        sarif=sarif,
        output_dir=output_dir,
    )

    # -------------------------
    # HTML Report
    # -------------------------

    findings = []

    for _, report in reports:
        findings.extend(report.findings)

    generate_html_report(
        findings=findings,
        output_dir=output_dir,
    )
    save_scan_json(
        reports=reports,
        output_dir=output_dir,
    )

    # -------------------------
    # Future Reports
    # -------------------------

    # save_json(...)