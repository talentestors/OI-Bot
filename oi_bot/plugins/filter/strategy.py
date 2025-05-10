# Author: telenterstors
# Created: 2025-03-31
# Description: This module provides a filter class to filter messages based on a given strategy.
# License: AGPL-3.0

from typing import override
from .strategy_base import FilterStrategy, ReplaceStrategy


# Filter strategy module
class FilterStrategyAllowAll(FilterStrategy):
    """
    A filter strategy that allows all messages.
    """

    @override
    def filter(self, message) -> bool:
        """
        Allow all messages.
        """
        return True


class FilterStrategyDenyAll(FilterStrategy):
    """
    A filter strategy that denies all messages.
    """

    @override
    def filter(self, message) -> bool:
        """
        Deny all messages.
        """
        return False


class FilterStrategyAllowList(FilterStrategy):
    """
    A filter strategy that allows messages in a list.
    """

    def __init__(self, allow_list):
        self.allow_list = allow_list

    @override
    def filter(self, message) -> bool:
        """
        Allow messages in the list.
        """
        return message in self.allow_list


class FilterStrategyDenyList(FilterStrategy):
    """
    A filter strategy that denies messages in a list.
    """

    def __init__(self, deny_list):
        self.deny_list = deny_list

    @override
    def filter(self, message) -> bool:
        """
        Deny messages in the list.
        """
        return message not in self.deny_list


class FilterStrategyRegex(FilterStrategy):
    """
    A filter strategy that uses a regular expression to filter messages.
    """

    def __init__(self, pattern):
        self.pattern = pattern

    @override
    def filter(self, message) -> bool:
        """
        Filter messages using a regular expression.
        """
        import re

        return re.match(self.pattern, message) is not None


class FilterStrategyFunction(FilterStrategy):
    """
    A filter strategy that uses a function to filter messages.
    """

    def __init__(self, function):
        self.function = function

    @override
    def filter(self, message) -> bool:
        """
        Filter messages using a function.
        """
        return self.function(message)


# Replace strategy module
class ReplaceStrategyNoReplace(ReplaceStrategy):
    """
    A replace strategy that does not replace the message.
    """

    @override
    def replace(self, message):
        """
        Do not replace the message.
        """
        return message


class ReplaceStrategyReplace(ReplaceStrategy):
    """
    A replace strategy that replaces the message with a new one.
    """

    def __init__(self, new_message):
        self.new_message = new_message

    @override
    def replace(self, message):
        """
        Replace the message with a new one.
        """
        return self.new_message


class ReplaceStrategyReplaceWithRegex(ReplaceStrategy):
    """
    A replace strategy that replaces the message using a regular expression.
    """

    def __init__(self, pattern, replacement):
        self.pattern = pattern
        self.replacement = replacement

    @override
    def replace(self, message):
        """
        Replace the message using a regular expression.
        """
        import re

        return re.sub(self.pattern, self.replacement, message)


class ReplaceStrategyReplaceWithFunction(ReplaceStrategy):
    """
    A replace strategy that replaces the message using a function.
    """

    def __init__(self, function):
        self.function = function

    @override
    def replace(self, message):
        """
        Replace the message using a function.
        """
        return self.function(message)


# End of file
