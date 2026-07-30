import json
from pathlib import Path

from schemas.findings import ReviewReport


def generate_json(report: ReviewReport) -> dict:
    """
    Convert ReviewReport into JSON serializable dict.
    """

    return report.model_dump()


def save_json(
    report: ReviewReport,
    filename: str,
    output_dir: Path,
) -> Path:
    """
    Save JSON report.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            generate_json(report),
            f,
            indent=4,
            ensure_ascii=False,
        )

    return path


def generate_scan_json(
    reports: list[tuple[str, ReviewReport]],
) -> dict:

    output = {
        "summary": {
            "total_files": len(reports),
            "total_findings": 0,
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        },
        "reports": [],
    }

    for filename, report in reports:

        output["reports"].append(
            {
                "file": filename,
                "summary": report.summary.model_dump(),
                "findings": [
                    finding.model_dump()
                    for finding in report.findings
                ],
            }
        )

        output["summary"]["total_findings"] += report.summary.total_findings
        output["summary"]["critical"] += report.summary.critical
        output["summary"]["high"] += report.summary.high
        output["summary"]["medium"] += report.summary.medium
        output["summary"]["low"] += report.summary.low
        output["summary"]["info"] += report.summary.info

    return output


def save_scan_json(
    reports: list[tuple[str, ReviewReport]],
    output_dir: Path,
) -> Path:

    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / "report.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            generate_scan_json(reports),
            f,
            indent=4,
            ensure_ascii=False,
        )

    return path