"""Experience filter implementation."""

from .base_filter import BaseFilter
from ..candidate import Candidate


class ExperienceFilter(BaseFilter):
    """
    Filter candidates by years of experience.

    Candidates must have experience within the specified range (inclusive).
    Default range: 1-3 years.
    """

    def __init__(self, min_years: float = 1.0, max_years: float = 3.0):
        """
        Initialize the experience filter.

        Args:
            min_years: Minimum years of experience (inclusive)
            max_years: Maximum years of experience (inclusive)
        """
        self.min_years = min_years
        self.max_years = max_years

    def apply(self, candidate: Candidate) -> bool:
        """
        Check if candidate's experience is within the specified range.

        Args:
            candidate: The candidate to evaluate

        Returns:
            True if candidate's experience is between min_years and max_years (inclusive)
        """
        return self.min_years <= candidate.experience_years <= self.max_years

    def __repr__(self) -> str:
        return f"<ExperienceFilter: {self.min_years}-{self.max_years} years>"
