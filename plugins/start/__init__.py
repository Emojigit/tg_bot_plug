__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/tg_bot_plug"
__description__ = "Example of plugin"
__dname__ = "start"

from telethon import events
def setup(bot,storage):
    @bot.on(events.NewMessage(pattern='/start'))
    async def start(event):
        """Send a message when the command /start is issued."""
        executed_times = storage.get("exectimes",0)
        executed_times += 1
        await event.respond('Hello, I am a bot!\nBot powered by Telegram Bot Plug\nExecuted: ' + str(executed_times))
        storage.set("exectimes", executed_times)
        raise events.StopPropagation

