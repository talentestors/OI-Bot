import pytest
from nonebug import App
from nonebot.log import logger

from .utils import make_event


@pytest.mark.asyncio
async def test_about(app: App):
    from oi_bot.plugins.about import about, about_cn, get_about_msg

    logger.info("Test about starting")
    async with app.test_matcher(about) as ctx:
        event = make_event("/about")
        msg = get_about_msg("en")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(about)

    async with app.test_matcher(about_cn) as ctx:
        event = make_event("/关于")
        msg = get_about_msg("cn")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(about_cn)
