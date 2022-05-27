__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/tg_bot_plug"
__description__ = "Example of plugin"
__dname__ = "start"
__moreinfo__ = ["Example __moreinfo__"]

from telethon import events
import config
def setup(bot,storage):
    @bot.on(events.NewMessage(pattern='/start'))
    async def start(event):
        """Send a message when the command /start is issued."""
        executed_times = storage.get("exectimes",0)
        executed_times += 1
        await event.respond('Hello, I am a bot!\nBot powered by Telegram Bot Plug\nExecuted: ' + str(executed_times))
        if config.owner == event.sender.id:
            await event.respond('Welcome back, owner.')
        storage.set("exectimes", executed_times)
        raise events.StopPropagation

