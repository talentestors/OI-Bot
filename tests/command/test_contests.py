import pytest
from nonebug import App
from nonebot.log import logger

from tests.utils import make_event

@pytest.mark.asyncio
async def test_today_contests(app: App):
    from oi_bot.plugins.command import today_contest

    logger.info("Test today_contests starting")
    async with app.test_matcher(today_contest) as ctx:
        bot = ctx.create_bot()
        event = make_event("/今日比赛")
        ctx.receive_event(bot, event)
        ctx.should_finished(today_contest)

    logger.info("Test today_contests passed")
