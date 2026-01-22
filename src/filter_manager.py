"""Filter manager for orchestrating multiple filters."""

from typing import List, Dict, Optional

from .candidate import Candidate
from .filters.base_filter import BaseFilter


class FilterManager:
    """
    Manages a collection of filters and applies them to candidates.

    Supports dynamic addition/removal of filters and provides
    detailed filtering results.
    """

    def __init__(self):
        """Initialize the filter manager with an empty filter list."""
        self._filters: Dict[str, BaseFilter] = {}

    def add_filter(self, filter_instance: BaseFilter) -> None:
        """
        Add a filter to the manager.

        Args:
            filter_instance: The filter to add
        """
        self._filters[filter_instance.name] = filter_instance

    def remove_filter(self, filter_name: str) -> Optional[BaseFilter]:
        """
        Remove a filter by name.

        Args:
            filter_name: Name of the filter to remove

        Returns:
            The removed filter, or None if not found
        """
        return self._filters.pop(filter_name, None)

    def get_filter(self, filter_name: str) -> Optional[BaseFilter]:
        """
        Get a filter by name.

        Args:
            filter_name: Name of the filter

        Returns:
            The filter, or None if not found
        """
        return self._filters.get(filter_name)

    def list_filters(self) -> List[str]:
        """
        List all registered filter names.

        Returns:
            List of filter names
        """
        return list(self._filters.keys())

    def apply_all(self, candidates: List[Candidate]) -> List[Candidate]:
        """
        Apply all filters to a list of candidates.

        A candidate must pass ALL filters to be included in the result.

        Args:
            candidates: List of candidates to filter

        Returns:
            List of candidates that pass all filters
        """
        if not self._filters:
            return candidates

        result = []
        for candidate in candidates:
            if self._passes_all_filters(candidate):
                result.append(candidate)
        return result

    def apply_all_with_details(
        self, candidates: List[Candidate]
    ) -> Dict[str, List[Candidate]]:
        """
        Apply all filters and return detailed results.

        Args:
            candidates: List of candidates to filter

        Returns:
            Dictionary with:
                - 'passed': Candidates that passed all filters
                - 'failed_<filter_name>': Candidates that failed each specific filter
        """
        result = {
            'passed': [],
            **{f'failed_{name}': [] for name in self._filters.keys()}
        }

        for candidate in candidates:
            passed_all = True
            for name, filter_instance in self._filters.items():
                if not filter_instance.apply(candidate):
                    result[f'failed_{name}'].append(candidate)
                    passed_all = False

            if passed_all:
                result['passed'].append(candidate)

        return result

    def _passes_all_filters(self, candidate: Candidate) -> bool:
        """
        Check if a candidate passes all filters.

        Args:
            candidate: The candidate to check

        Returns:
            True if candidate passes all filters
        """
        for filter_instance in self._filters.values():
            if not filter_instance.apply(candidate):
                return False
        return True

    def __len__(self) -> int:
        """Return the number of registered filters."""
        return len(self._filters)

    def __repr__(self) -> str:
        return f"<FilterManager: {len(self._filters)} filters>"
