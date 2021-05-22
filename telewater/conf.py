""" This module defines the constants or default values.
"""
from pydantic import BaseModel, validator


class Config(BaseModel):
    watermark: str = "https://telegra.ph/file/7bdb50d361c083f3970db.png"
    x_off: int = 10
    y_off: int = 10
    frame_rate: int = 15
    preset: str = "ultrafast"

    @validator("preset")
    def validate_preset(val):
        allowed = ["ultrafast", "fast", "medium", "slow"]
        if not val in allowed:
            raise ValueError(f"Choose preset from {allowed}")
        return val

START = """Bot to add Watermark to Photos, Videos & GIFs.

Channel: @ARNextRobot


**Developed with ❤️ by @SarahMaiaOff**

"""

HELP = """
Using the bot is very simple. Just send a photo, video or gif to the bot. The bot will reply with the watermarked media.

The bot commands `/set` and `/get` can set and get the value of the configuration variables. The commands are simple and intuitive. The bot will show you the usage if you send an incorrect argument.

Syntax for `/set` ➜  `/set key: value`
Syntax for `/get` ➜  `/get key`

"""

COMMANDS = {
    "start": "start the bot or check if alive",
    "set": "set the value for a config variable",
    "get": "know the value of a config variable",
    "help": "learn how to use the bot",
}

config = Config()
