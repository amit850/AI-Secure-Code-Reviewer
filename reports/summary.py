# ==========================================================
# Scan Summary Report Generator
# ==========================================================

from pathlib import Path

from schemas.findings import ReviewReport


def generate_summary(
    reports: list[tuple[str, ReviewReport]]
) -> str:
    """
    Generate a summary markdown for the complete scan.
    """

    total_files = len(reports)

    total_findings = 0
    critical = 0
    high = 0
    medium = 0
    low = 0
    info = 0

    md = "# AI Secure Code Review Summary\n\n"

    md += f"Files Scanned: **{total_files}**\n\n"

    md += "## Files\n\n"

    for filename, report in reports:

        md += f"- {filename}\n"

        total_findings += report.summary.total_findings
        critical += report.summary.critical
        high += report.summary.high
        medium += report.summary.medium
        low += report.summary.low
        info += report.summary.info

    md += "\n---\n\n"

    md += "## Findings Summary\n\n"

    md += f"- Total Findings: {total_findings}\n"
    md += f"- Critical: {critical}\n"
    md += f"- High: {high}\n"
    md += f"- Medium: {medium}\n"
    md += f"- Low: {low}\n"
    md += f"- Info: {info}\n"

    return md


def save_summary(
    markdown: str,
    output_dir: Path
) -> Path:

    output_file = output_dir / "summary.md"

    output_file.write_text(
        markdown,
        encoding="utf-8"
    )

    return output_file