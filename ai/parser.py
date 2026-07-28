import json

from ai.normalizer import normalize_response
from schemas.findings import ReviewReport


def parse_review(response: str) -> ReviewReport:
    data = json.loads(response)

    data = normalize_response(data)

    return ReviewReport.model_validate(data)