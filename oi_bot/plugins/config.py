from pydantic import BaseModel, Field


class Config(BaseModel):
    bot_enable_console: bool = Field(default=False, description="Enable console")

