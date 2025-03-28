from pydantic import BaseModel


class Config(BaseModel):
    bot_enable_console: bool = False

