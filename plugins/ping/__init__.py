# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/tg_bot_plug"
__description__ = "Ping Pong!"
__dname__ = "ping"

randoms = [
    "Ping Pong!",
    "Table Tennis!",
    "Sports!",
]

import random
from telethon import events
def setup(bot):
    @bot.on(events.NewMessage(pattern='/ping'))
    async def ping(event):
        await event.respond("🏓 " + random.choice(randoms))
        raise events.StopPropagation

