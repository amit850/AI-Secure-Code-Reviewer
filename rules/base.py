"""
Base Rule

Every detection rule must inherit from this class.
"""

from abc import ABC, abstractmethod


class Rule(ABC):
    """
    Abstract base class for all security rules.
    """

    @abstractmethod
    def scan(
        self,
        file_path: str,
        source_code: str
    ) -> list[dict]:
        """
        Scan the source code.

        Returns:
            List of findings.
        """

        pass