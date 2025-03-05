from datetime import datetime

from nonebot.adapters.console import User, Message, MessageEvent

def make_event(message: str = "") -> MessageEvent:
    return MessageEvent(
        time=datetime.now(),
        self_id="test",
        message=Message(message),
        user=User(id="user"),
    )
