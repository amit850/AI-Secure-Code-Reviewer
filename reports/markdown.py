# ==========================================================
# Markdown Report Generator
# ==========================================================

from pathlib import Path

from config import REPORT_FOLDER
from schemas.findings import ReviewReport


def generate_markdown(report: ReviewReport) -> str:
    """
    Convert ReviewReport into Markdown.
    """

    md = "# AI Secure Code Review Report\n\n"

    md += "## Summary\n\n"

    md += f"- Total Findings: {report.summary.total_findings}\n"
    md += f"- Critical: {report.summary.critical}\n"
    md += f"- High: {report.summary.high}\n"
    md += f"- Medium: {report.summary.medium}\n"
    md += f"- Low: {report.summary.low}\n"
    md += f"- Info: {report.summary.info}\n\n"

    md += "---\n\n"

    if not report.findings:
        md += "## ✅ No security vulnerabilities found.\n"
        return md

    md += "## Findings\n\n"

    for index, finding in enumerate(report.findings, start=1):

        md += f"### {index}. {finding.title}\n\n"

        md += f"- Severity: **{finding.severity}**\n"
        md += f"- Confidence: **{finding.confidence}**\n"
        md += f"- CWE: {finding.cwe}\n"
        md += f"- OWASP: {finding.owasp}\n"
        md += f"- File: {finding.file}\n"
        md += f"- Line: {finding.line}\n\n"

        md += f"**Description**\n\n{finding.description}\n\n"

        md += f"**Evidence**\n\n{finding.evidence}\n\n"

        md += f"**Recommendation**\n\n{finding.recommendation}\n\n"

        md += "**Secure Code Example**\n\n"

        md += "```text\n"
        md += finding.secure_code_example
        md += "\n```\n\n"

        md += "---\n\n"

    return md


def save_markdown(
    markdown: str,
    filename: str = "review.md",
    output_dir: Path | None = None
) -> Path:
    """
    Save markdown report to disk.
    """

    if output_dir is None:
        output_dir = Path(REPORT_FOLDER)

    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / filename

    output_file.write_text(
        markdown,
        encoding="utf-8"
    )

    return output_file