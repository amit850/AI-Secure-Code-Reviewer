"""
Base Rule

Every detection rule must inherit from this class.
"""

from abc import ABC, abstractmethod


class BaseRule(ABC):
    """
    Abstract base class for all security rules.
    """

    id = ""
    name = ""
    description = ""

    @abstractmethod
    def scan(self, filename: str, code: str):
        """
        Scan source code and return a list of findings.
        """
        pass