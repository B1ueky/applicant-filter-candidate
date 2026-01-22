"""Location filter implementation."""

from typing import List

from .base_filter import BaseFilter
from ..candidate import Candidate


class LocationFilter(BaseFilter):
    """
    Filter candidates by location.

    Excludes candidates from specified locations.
    Default excluded location: Sydney.
    """

    def __init__(self, excluded_locations: List[str] = None):
        """
        Initialize the location filter.

        Args:
            excluded_locations: List of locations to exclude (case-insensitive)
        """
        if excluded_locations is None:
            excluded_locations = ["Sydney"]
        self.excluded_locations = [loc.lower() for loc in excluded_locations]

    def apply(self, candidate: Candidate) -> bool:
        """
        Check if candidate is NOT from an excluded location.

        Args:
            candidate: The candidate to evaluate

        Returns:
            True if candidate's location is NOT in the excluded list
        """
        return candidate.location.lower() not in self.excluded_locations

    def __repr__(self) -> str:
        return f"<LocationFilter: excludes {self.excluded_locations}>"
