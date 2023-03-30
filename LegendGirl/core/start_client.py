import platform

from pyrogram import __version__ as py_version
from pyrogram import idle

version = "v1.0"
group_username = "@RONNY_KI_DUNIYA"
from LegendBS.start_bot import start_bot

from LegendGirl.Config import *

from .clients import *

if Client1:
    pass


def Start_BotSpam():
    for i in range(1, 26):
        var = globals()[f"Client{i}"]
        if var is not None:
            start_bot(var)
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"🔥 Bot Shiv Spam 🔥[INFO] : Group Username {group_username}")
    print(f"🔥 Bot Shiv Spam 🔥[INFO] : Version - {platform.python_version()}")
    print(f"🔥 Bot Shiv Spam 🔥[INFO]: SpamBot Version - {version}")
    print(f"🔥 Bot Shiv Spam 🔥[INFO]: Pyrogram Version - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    idle()
