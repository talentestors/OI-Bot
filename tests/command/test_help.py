import pytest
from nonebug import App
from nonebot.log import logger

from .utils import make_event


@pytest.mark.asyncio
async def test_show_menu(app: App):
    from oi_bot.plugins.help_help import help, get_show_menu

    logger.info("Test show_menu starting")
    msg = get_show_menu()

    async with app.test_matcher(help) as ctx:
        event = make_event("/help")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(help)

    async with app.test_matcher(help) as ctx:
        event = make_event("/帮助")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(help)
