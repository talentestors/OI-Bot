from nonebot import on_command
from nonebot.rule import to_me

from nonebot_plugin_oi_helper.query_api import (
    get_dirs,
    get_today_contests,
    get_tomorrow_contests,
    get_now_contests,
    get_upcoming_contests,
    get_luogu_newest_news,
    get_luogu_random_news,
    get_leetcode_daily,
    json2text_for_leetcode_daily_info,
    json2text,
    json2text_get_luogu_news_text,
    json2text_for_contest,
)

dirs = get_dirs()

format_contests = json2text(json2text_for_contest)
format_leetcode = json2text(json2text_for_leetcode_daily_info)
format_luogu = json2text(json2text_get_luogu_news_text)

# Commands

today_contest = on_command("今日比赛", rule=to_me(), priority=5, block=True)


@today_contest.handle()
async def handle_today_contests():
    res = format_contests(await get_today_contests())
    if res == "":
        res = "今天没有比赛哦！"
    res = f"Today's Contest:\n{res}"
    await today_contest.finish(res)


tomorrow_contests = on_command("明日比赛", rule=to_me(), priority=5, block=True)


@tomorrow_contests.handle()
async def handle_tomorrow_contests():
    res = format_contests(await get_tomorrow_contests())
    if res == "":
        res = "明天没有比赛哦！"
    res = f"Tomorrow's Contest:\n{res}"
    await tomorrow_contests.finish(res)


now_contests = on_command(
    "正在进行的比赛",
    rule=to_me(),
    priority=10,
    block=True,
)


@now_contests.handle()
async def handle_now_contests():
    res = format_contests(await get_now_contests())
    if res == "":
        res = "现在还没有比赛在进行哦！"
    res = f"正在进行的比赛:\n{res}"
    await now_contests.finish(res)


upcoming_contests = on_command(
    "即将开始的比赛",
    rule=to_me(),
    priority=10,
    block=True,
)


@upcoming_contests.handle()
async def handle_upcoming_contests():
    res = format_contests(await get_upcoming_contests())
    if res == "":
        res = "未来没有比赛哦！"
    res = f"即将开始的比赛:\n{res}"
    await upcoming_contests.finish(res)


leetcode_daily = on_command(
    "力扣每日一题",
    rule=to_me(),
    priority=5,
    block=True,
)


@leetcode_daily.handle()
async def handle_leetcode_daily():
    res = format_leetcode(await get_leetcode_daily())
    await leetcode_daily.finish(res)


luogu_news = on_command(
    "洛谷日报",
    rule=to_me(),
    priority=10,
    block=True,
)


@luogu_news.handle()
async def handle_luogu_news():
    res = format_luogu(await get_luogu_newest_news())
    if res == "":
        res = "无"
    res = f"洛谷日报:\n{res}"
    await luogu_news.finish(res)


luogu_random_news = on_command(
    "随机洛谷日报",
    rule=to_me(),
    priority=8,
    block=True,
)


@luogu_random_news.handle()
async def handle_luogu_random_news():
    res = format_luogu(await get_luogu_random_news())
    await luogu_random_news.finish(res)
