from nonebug import App
from nonebot.log import logger
from .utils import make_event


async def test_today_contest(app: App):
    from nonebot_plugin_oi_helper.command import (
        today_contest,
        get_today_contests,
        format_contests,
    )

    msg = format_contests(await get_today_contests())
    if msg == "":
        msg = "今天没有比赛哦！"
    msg = f"Today's Contest:\n{msg}"
    logger.trace(msg)

    async with app.test_matcher(today_contest) as ctx:
        event = make_event("/今日比赛")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(today_contest)


async def test_tomorrow_contests(app: App):
    from nonebot_plugin_oi_helper.command import (
        tomorrow_contests,
        get_tomorrow_contests,
        format_contests,
    )

    msg = format_contests(await get_tomorrow_contests())
    if msg == "":
        msg = "明天没有比赛哦！"
    msg = f"Tomorrow's Contest:\n{msg}"
    logger.trace(msg)

    async with app.test_matcher(tomorrow_contests) as ctx:
        event = make_event("/明日比赛")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(tomorrow_contests)


async def test_leetcode_daily(app: App):
    from nonebot_plugin_oi_helper.command import (
        leetcode_daily,
        get_leetcode_daily,
        format_leetcode,
    )

    msg = format_leetcode(await get_leetcode_daily())
    logger.trace(msg)

    async with app.test_matcher(leetcode_daily) as ctx:
        event = make_event("/每日一题")
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, msg, result=None)
        ctx.should_finished(leetcode_daily)


async def test_luogu_news(app: App):
    assert True, "Not implemented yet"
