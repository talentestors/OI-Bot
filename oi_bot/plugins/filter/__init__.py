# none_plugin_oi_helper.filter for NoneBot2 plugin
# Copyright (C) 2025  talentestors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from re import L
from typing import Any
import contextlib
from nonebot.adapters import Bot
from .filter import Filter
from .strategy import ReplaceStrategyReplaceWithRegex
from nonebot.log import logger


def replace_func(match):
    header = match.group(1) or ""
    host = match.group(2)
    host = host.rstrip("_").replace(".", "_")
    port = match.group(3) or ""
    path = match.group(4) or ""
    return f"{header}{host}{port}{path}"


replace_strategy = ReplaceStrategyReplaceWithRegex(
    r"^(https?://)?([a-zA-Z0-9._-]+)(:[0-9]+)?(/.*)?", replace_func
)

filters = Filter(strategy_of_replace=replace_strategy)


@Bot.on_calling_api
async def handle_filter(bot: Bot, api: str, data: dict[str, Any]):
    with contextlib.suppress(Exception):
        # if api not in ["send_msg", "send_message"]:
        #     return
        # if len(data["message"]) != 1 or data["message"][0].type != "text":
        #     return
        text = str(data["message"][0].data["text"])
        logger.info(f"handle_filter: {text}")
        # 处理文本消息
        new_message = filters.replace(text)
        logger.info(f"handle_filter: {new_message}")
        data["message"] = new_message
