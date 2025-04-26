# about.py: The about plugin of the bot.
# Author: talentestors
# Created: 2025-03-13

from nonebot import on_command
from nonebot.rule import to_me


def get_about_msg(lang: str) -> str:
    """Get the self introduction of the bot.

    Returns:
        str: The self introduction of the bot.

    Example:
    >>> print(get_about_msg("en"))
    About the bot:
    Hi, I am a QQ bot based on nonebot2. I am developed by talentestors.
    I can provide match information for OIer and ACMer.
    I am still under development, so there may be some bugs.
    If you have any questions or suggestions, please submit an issue on repository.
    The repository of the bot is:
    https://github.com/talentestors/OI-Bot
    >>> print(get_about_msg("cn"))
    关于机器人：
    Hi, 我是一个基于nonebot2的QQ机器人。
    我可以为OI和ACM选手提供比赛信息。
    我仍在开发中，所以可能会有一些bug。
    如果您有任何问题或建议，请在仓库上提交issue。
    机器人的仓库是：
    https://github.com/talentestors/OI-Bot
    """
    if lang not in ["cn", "en"]:
        lang = "en"
    ABOUT_MSG = """About the bot:
Hi, I am a QQ bot based on nonebot2. I am developed by talentestors.
I can provide match information for OIer and ACMer.
I am still under development, so there may be some bugs.
If you have any questions or suggestions, please submit an issue on repository.
The repository of the bot is:
https://github.com/talentestors/OI-Bot"""
    ABOUT_MSG_CN = """关于机器人：
Hi, 我是一个基于nonebot2的QQ机器人。
我可以为OIer和ACMer提供比赛信息。
我仍在开发中，所以可能会有一些bug。
如果您有任何问题或建议，请在仓库上提交issue。
机器人的仓库是：
https://github.com/talentestors/OI-Bot"""
    return lang == "cn" and ABOUT_MSG_CN or ABOUT_MSG


about = on_command("about", rule=to_me(), priority=1, block=True)


@about.handle()
async def handle_about(bot, event):
    await about.finish(get_about_msg("en"))

about_cn = on_command("关于", rule=to_me(), priority=1, block=True)


@about_cn.handle()
async def handle_about_cn(bot, event):
    await about_cn.finish(get_about_msg("cn"))
