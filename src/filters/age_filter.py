"""Age filter implementation."""

from .base_filter import BaseFilter
from ..candidate import Candidate


class AgeFilter(BaseFilter):
    """
    Filter candidates by age range.

    Candidates must be within the specified age range (inclusive).
    Default range: 20-40 years old.
    """

    def __init__(self, min_age: int = 20, max_age: int = 40):
        """
        Initialize the age filter.

        Args:
            min_age: Minimum age (inclusive)
            max_age: Maximum age (inclusive)
        """
        self.min_age = min_age
        self.max_age = max_age

    def apply(self, candidate: Candidate) -> bool:
        """
        Check if candidate's age is within the specified range.

        Args:
            candidate: The candidate to evaluate

        Returns:
            True if candidate's age is between min_age and max_age (inclusive)
        """
        return self.min_age <= candidate.age <= self.max_age

    def __repr__(self) -> str:
        return f"<AgeFilter: {self.min_age}-{self.max_age}>"
