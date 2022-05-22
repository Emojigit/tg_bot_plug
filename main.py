import sys, asyncio, importlib
from telethon import TelegramClient, functions, types, events
from telethon.errors import *

exit = sys.exit

try:
    import config
except ImportError:
    print("config.py not found, copying one for you...")
    import shutil
    try:
        shutil.copyfile("config.example.py","config.py")
        print("Config file copied, follow the instructions inside to config the bot.")
    except FileNotFoundError:
        print("config.example.py not found, make sure you're in the script's directory!")
    exit(1)

bot = TelegramClient('bot', config.api_id, config.api_hash).start(bot_token=config.bot_token)
plugins = [importlib.import_module(plugin) for plugin in config.plugins_enabled]
for x in plugins:
    print("Loading plugin: {}".format(x.__name__))
    x.setup(bot)

txt_plugslist = []
txt_plugslist.append("List of plugins installed:")
for x in plugins:
    dirs = dir(x)
    name = x.__name__
    if "__dname__" in dirs:
        name = x.__dname__
    if "__url__" in dirs:
        txt_plugslist.append("[{}]({}): {}".format(name,x.__url__,x.__description__))
    else:
        txt_plugslist.append("{}: {}".format(name,x.__description__))
    txt_plugslist.append("- By {}, ver. {}".format(x.__author__,x.__version__))
txt_plugslist = "\n".join(txt_plugslist)

@bot.on(events.NewMessage(pattern='/plugslist'))
async def plugslist(event):
    await event.respond(txt_plugslist,link_preview=False)
    raise events.StopPropagation

print("Finished. Starting bot...")
bot.run_until_disconnected()

