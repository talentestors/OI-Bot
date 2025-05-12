# Author: telenterstors
# Created: 2025-03-31
# Description: This module provides a filter class to filter messages based on a given strategy.
# License: AGPL-3.0

from .strategy_base import FilterStrategy, ReplaceStrategy


class Filter(object):
    """
    A class to filter messages based on a given strategy.
    """

    def __init__(
        self,
        strategy_of_filter: FilterStrategy | None = None,
        strategy_of_replace: ReplaceStrategy | None = None,
    ) -> None:
        self.filter_strategy = strategy_of_filter
        self.replace_strategy = strategy_of_replace

    def filter(self, message) -> bool:
        """
        Filter the message using the current strategy.
        """
        if self.filter_strategy is None:
            return True
        return self.filter_strategy.filter(message)

    def replace(self, message):
        """
        Apply the replace strategy to the provided message and return the result.
        If no replace strategy is set, return the message unchanged.
        """
        if self.replace_strategy is None:
            return message
        return self.replace_strategy.replace(message)

    def set_strategy(self, strategy) -> None:
        """
        Set the filter strategy.
        """
        self.filter_strategy = strategy

    def set_replace_strategy(self, strategy) -> None:
        """
        Set the replace strategy.
        """
        self.replace_strategy = strategy

    def __str__(self) -> str:
        """
        Return a string representation of the filter.
        """
        return f"Filter(strategy_of_filter={self.filter_strategy}, strategy_of_replace={self.replace_strategy})"

    def __repr__(self) -> str:
        """
        Return a string representation of the filter.
        """
        return f"Filter(strategy_of_filter={self.filter_strategy}, strategy_of_replace={self.replace_strategy})"

    def __eq__(self, other) -> bool:
        """
        Check if two filters are equal.
        """
        if not isinstance(other, Filter):
            return False
        return (
            self.filter_strategy == other.filter_strategy
            and self.replace_strategy == other.replace_strategy
        )

    def __hash__(self) -> int:
        """
        Return a hash of the filter.
        """
        return hash((self.filter_strategy, self.replace_strategy))

    def __del__(self) -> None:
        """
        Delete the filter.
        """
        del self.filter_strategy
        del self.replace_strategy
        self.filter_strategy = None
        self.replace_strategy = None
