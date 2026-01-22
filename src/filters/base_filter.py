"""Base filter class for the extensible filter system."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..candidate import Candidate


class BaseFilter(ABC):
    """
    Abstract base class for candidate filters.

    To create a new filter:
    1. Inherit from BaseFilter
    2. Implement the apply() method
    3. Optionally override the name property

    Example:
        class MyCustomFilter(BaseFilter):
            def apply(self, candidate: Candidate) -> bool:
                return candidate.some_field == some_value
    """

    @property
    def name(self) -> str:
        """
        Return the name of the filter.
        Defaults to the class name without 'Filter' suffix.
        """
        class_name = self.__class__.__name__
        if class_name.endswith('Filter'):
            return class_name[:-6]
        return class_name

    @abstractmethod
    def apply(self, candidate: "Candidate") -> bool:
        """
        Apply the filter to a candidate.

        Args:
            candidate: The candidate to evaluate

        Returns:
            True if the candidate passes the filter, False otherwise
        """
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
