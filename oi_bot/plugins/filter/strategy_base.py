# Author: telenterstors
# Created: 2025-03-31
# Description: This module provides a filter class to filter messages based on a given strategy.
# License: AGPL-3.0

import abc


# Filter strategy module
class FilterStrategy(abc.ABC, object):
    """
    Abstract base class for filter strategies.
    """

    @abc.abstractmethod
    def filter(self, message) -> bool:
        """
        Abstract method to filter a message.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __repr__(self) -> str:
        """
        Return a string representation of the filter strategy.
        """
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        """
        Return a string representation of the filter strategy.
        """
        return f"{self.__class__.__name__}()"

    def __eq__(self, other) -> bool:
        """
        Check if two filter strategies are equal.
        """
        if not isinstance(other, FilterStrategy):
            return False
        return self.__class__ == other.__class__

    def __hash__(self) -> int:
        """
        Return a hash value for the filter strategy.
        """
        return hash(self.__class__.__name__)


# Replace strategy module
class ReplaceStrategy(abc.ABC, object):
    """
    Abstract base class for replace strategies.
    """

    @abc.abstractmethod
    def replace(self, message):
        """
        Abstract method to replace a message.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __repr__(self) -> str:
        """
        Return a string representation of the replace strategy.
        """
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        """
        Return a string representation of the replace strategy.
        """
        return f"{self.__class__.__name__}()"

    def __eq__(self, other) -> bool:
        """
        Check if two replace strategies are equal.
        """
        if not isinstance(other, ReplaceStrategy):
            return False
        return self.__class__ == other.__class__

    def __hash__(self) -> int:
        """
        Return a hash value for the replace strategy.
        """
        return hash(self.__class__.__name__)
