# help_help.py
# Author: talentestors
# Created on 2025-03-05

from nonebot import on_command
from nonebot.rule import to_me

# define the help menu
HELP_LIST = """HELP MENU:
1. 今日比赛: 获取今日比赛信息
2. 明日比赛: 获取明日比赛信息
3. 每日一题: 获取 LeetCode 每日一题
4. 抽签: 抽取今日运势
5. help: 获取帮助信息
6. about/关于: 获取机器人信息"""


def get_show_menu() -> str:
    """Get the help menu.

    Returns:
        str: The help menu.

    >>> print(get_show_menu())
    HELP MENU:
    1. 今日比赛: 获取今日比赛信息
    2. 明日比赛: 获取明日比赛信息
    3. 每日一题: 获取 LeetCode 每日一题
    4. 抽签: 抽取今日运势
    5. help: 获取帮助信息
    6. about/关于: 获取机器人信息
    """
    return HELP_LIST


help = on_command("help", aliases={"帮助"}, rule=to_me(), priority=1, block=True)


@help.handle()
async def handle_help(bot, event):
    await help.finish(get_show_menu())
