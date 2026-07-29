from pathlib import Path
from datetime import datetime


def create_scan_directory(base_folder: str) -> Path:
    """
    Create Unique folder for every scan.
    Example: reports/scan_20260730_233015/

    """
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    scan_dir=Path(base_folder) / f"scan_{timestamp}"
    scan_dir.mkdir(parents=True, exist_ok=True)

    return scan_dir