# show_menu.py
# Author: talentestors
# Created on 2025-03-05

# define the help menu
# - 今日比赛: 获取今日比赛信息
# - 明日比赛: 获取明日比赛信息
# - 每日一题: 获取 LeetCode 每日一题
# - 洛谷日报: 获取洛谷日报
# - luoguluck: 获取洛谷运势
# - help: 获取帮助信息
HELP_LIST = """HELP MENU:
1. 今日比赛: 获取今日比赛信息
2. 明日比赛: 获取明日比赛信息
3. 每日一题: 获取 LeetCode 每日一题
4. 洛谷日报: 获取洛谷日报
5. luoguluck: 获取洛谷运势
6. help: 获取帮助信息"""


def get_show_menu() -> str:
    """Get the help menu.

    Returns:
        str: The help menu.

    >>> print(get_show_menu())
    HELP MENU:
    1. 今日比赛: 获取今日比赛信息
    2. 明日比赛: 获取明日比赛信息
    3. 每日一题: 获取 LeetCode 每日一题
    4. 洛谷日报: 获取洛谷日报
    5. luoguluck: 获取洛谷运势
    6. help: 获取帮助信息
    """
    return HELP_LIST
