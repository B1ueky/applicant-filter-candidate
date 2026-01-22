"""Background filter implementation."""

from typing import List

from .base_filter import BaseFilter
from ..candidate import Candidate


class BackgroundFilter(BaseFilter):
    """
    Filter candidates by educational and work background.

    Candidates must have background in preferred regions (中文或英文背景)
    and must NOT have background in excluded regions (India/Middle East).
    """

    def __init__(
        self,
        preferred_backgrounds: List[str] = None,
        excluded_backgrounds: List[str] = None
    ):
        """
        Initialize the background filter.

        Args:
            preferred_backgrounds: List of preferred countries/regions (中文和英文背景)
            excluded_backgrounds: List of excluded countries/regions
        """
        if preferred_backgrounds is None:
            preferred_backgrounds = [
                # 中文背景
                "China", "Taiwan", "Hong Kong", "Macau", "Singapore",
                # 英文背景
                "UK", "United Kingdom", "England", "Australia", "New Zealand", "USA", "Canada"
            ]

        if excluded_backgrounds is None:
            excluded_backgrounds = [
                # South Asia
                "India", "Pakistan", "Bangladesh",
                # Middle East
                "Saudi Arabia", "UAE", "United Arab Emirates", "Qatar", "Kuwait",
                "Bahrain", "Oman", "Iran", "Iraq", "Jordan", "Lebanon", "Syria",
                "Yemen", "Egypt", "Israel", "Palestine"
            ]

        self.preferred_backgrounds = [bg.lower() for bg in preferred_backgrounds]
        self.excluded_backgrounds = [bg.lower() for bg in excluded_backgrounds]

    def apply(self, candidate: Candidate) -> bool:
        """
        Check if candidate has appropriate background.

        Criteria:
        1. Must have at least one preferred background (中文或英文背景)
        2. Must NOT have any excluded background (India/Middle East)

        Args:
            candidate: The candidate to evaluate

        Returns:
            True if candidate meets both criteria
        """
        all_backgrounds = [
            bg.lower()
            for bg in candidate.education_background + candidate.work_background
        ]

        # Check for excluded backgrounds first
        for bg in all_backgrounds:
            if bg in self.excluded_backgrounds:
                return False

        # Check for at least one preferred background
        for bg in all_backgrounds:
            if bg in self.preferred_backgrounds:
                return True

        return False

    def __repr__(self) -> str:
        return f"<BackgroundFilter: prefers {self.preferred_backgrounds[:2]}..., excludes {len(self.excluded_backgrounds)} regions>"
