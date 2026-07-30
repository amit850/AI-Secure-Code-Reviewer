"""
SARIF Report Generator

Generates SARIF 2.1.0 compatible reports.
"""

import json
from pathlib import Path

from schemas.findings import ReviewReport


SARIF_LEVEL = {
    "Critical": "error",
    "High": "error",
    "Medium": "warning",
    "Low": "note",
    "Info": "note",
}


def generate_sarif(
    reports: list[tuple[str, ReviewReport]]
) -> dict:

    rules = []
    results = []

    rule_map = {}

    for _, report in reports:

        for finding in report.findings:

            rule_id = finding.cwe

            if rule_id not in rule_map:

                rule_map[rule_id] = len(rules)

                rules.append(
                    {
                        "id": rule_id,
                        "name": finding.title,
                        "shortDescription": {
                            "text": finding.title
                        },
                        "help": {
                            "text": finding.description
                        },
                        "properties": {
                            "owasp": finding.owasp,
                            "confidence": finding.confidence,
                        },
                    }
                )

            results.append(
                {
                    "ruleId": rule_id,
                    "ruleIndex": rule_map[rule_id],
                    "level": SARIF_LEVEL.get(
                        finding.severity,
                        "warning",
                    ),
                    "message": {
                        "text": finding.description
                    },
                    "locations": [
                        {
                            "physicalLocation": {
                                "artifactLocation": {
                                    "uri": finding.file
                                },
                                "region": {
                                    "startLine": finding.line
                                },
                            }
                        }
                    ],
                }
            )

    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": "AI Secure Code Reviewer",
                        "version": "2.5",
                        "rules": rules,
                    }
                },
                "results": results,
            }
        ],
    }


def save_sarif(
    sarif: dict,
    output_dir: Path,
    filename: str = "results.sarif",
):

    output = output_dir / filename

    with open(
        output,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            sarif,
            f,
            indent=4,
        )

    return output