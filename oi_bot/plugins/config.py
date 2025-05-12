from pydantic import BaseModel, Field


class Config(BaseModel):
    bot_enable_console: bool = Field(default=False, description="Enable console")
    bot_url_filter_enable: bool = Field(default=False, description="Enable URL filter")
