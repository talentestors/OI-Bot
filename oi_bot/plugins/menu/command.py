# command.py
# Author: talentestors
# Created on 2025-03-05

from nonebot import on_command
from nonebot.rule import to_me

from oi_bot.plugins.menu.show_menu import get_show_menu

help = on_command("help", rule=to_me(), priority=1, block=True)


@help.handle()
async def handle_help(bot, event):
    await help.finish(get_show_menu())
