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

import nonebot
from typing import Any
from nonebot.adapters import Bot, MessageSegment
from nonechat.message import ConsoleMessage, Text
from nonebot.log import logger

from .filter import Filter

env_config = nonebot.get_driver().config

# BOT_URL_FILTER_ENABLE
bot_url_filter_enable: bool = env_config.bot_url_filter_enable

if bot_url_filter_enable:
    from .strategy import ReplaceStrategyReplaceWithRegex

    def replace_func(match):
        header = match.group(1) or ""
        host = match.group(2)
        host = host.rstrip("_").replace(".", "_")
        port = match.group(3) or ""
        path = match.group(4) or ""
        return f"{header}{host}{port}{path}"

    replace_strategy = ReplaceStrategyReplaceWithRegex(
        r"(https?://)([a-zA-Z0-9._\-]+)(:\d+)?(/[^\s]*)?", replace_func
    )

    filters = Filter(strategy_of_replace=replace_strategy)

    logger.debug(f"filters: {filters}")

    def _filter_message_contents(contents: list[Any]) -> list[Any]:
        new_list: list[Any] = []
        for item in contents:
            match item:
                case Text():
                    new_list.append(Text(filters.replace(item.text)))
                case str():
                    new_list.append(filters.replace(item))
                case MessageSegment() if item.type == "text":
                    item.data["text"] = filters.replace(item.data["text"])
                    new_list.append(item)
                case _:
                    logger.error(f"Unknown message type: {type(item)}")
                    raise TypeError(f"Unknown message type: {type(item)}")
        return new_list

    @Bot.on_calling_api
    async def url_filter(bot: Bot, api: str, data: dict[str, Any]):
        logger.debug(f"API called: {api}, data: {data}")
        if api != "send_msg" or "message" not in data:
            return
        message = data["message"]
        match message:
            case ConsoleMessage():
                message.content = filter_message_contents(message.content)
            case list():
                data["message"] = filter_message_contents(message)
            case _:
                logger.error(f"Unknown message type: {type(message)}")
                raise TypeError(f"Unknown message type: {type(message)}")
