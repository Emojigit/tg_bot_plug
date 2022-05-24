## 如何建立一個插件
首先，在 `plugins` 目錄建立一個資料夾，名稱爲你的插件名稱，~~強烈建議同步放上GitHub~~
```bash
cd plugins
# GitHub CLI
gh repo create 插件的名字
# 或者選擇不發佈
mkdir 插件的名字
```
然後，創建 `__init__.py`， 在頂部塞這些：
```py
# -*- coding: utf-8 -*-

__author__ = "你的網名或名字"
__version__ = "1.0.0" # 版本號，建議 0.0.1 或者 1.0.0
__url__ = "https://example.com" # URL，如果不想發佈可省略
__description__ = "Join repeat" # 插件描述
__dname__ = "插件的名字"

from telethon import events
# 如果需要調用其他庫可以在這裏定義
def setup(bot,storage):
    # 主代碼！
```
### 如何建立主代碼
參看[Telethon API](https://docs.telethon.dev)，裏面的 `client` 或者 `bot` 就是 `def setup` 提供的那個。以下是一些例子：
#### 簡單指令
```py
@bot.on(events.NewMessage(pattern='/mycommand')) # mycommand == 命令名字
    async def mycommand(event):
        await event.respond("你好，世界。") # 使用 event.respond 在同一個聊天室回覆
    raise events.StopPropagation # 沒有必要讓其他插件繼續處理這一條信息（
```
#### 別人喵我也喵
首先，通過[@botfather](https://t.me/botfather)將機器人的隱私模式關閉。
```py
@bot.on(events.NewMessage()) # 匹配所有信息
    async def meou_reply(event):
        if "喵" in event.message.text: # 如果信息裏有喵
            await event.respond("喵～") # 那麼我們也喵～
```
#### 調用設定檔案
由於設定檔在 `config.py`，而開發者已經非常貼心的把專案目錄加到 `sys.path` 中，所以可以直接以調用庫的方式調用設定檔：
```py
import config
```
之後就可以使用了：
```py
# 獲取 BOT TOKEN
print(config.bot_token)
# 也可以自定義設定值，但記得提醒維護者設定
try:
    print(config.custom_whatever) # custom_whatever == 設定值
except AttributeError:
    print("主人，記得設定 config.custom_whatever 哦喵～") # 買萌換取主人注意（
    raise # 最後撒嬌（
```
### 錯誤處理
如在載入期間發生錯誤，程序並不會被中斷，而是直接暫時禁用插件，而且會在 `/plugslist` 指令顯示插件出錯，來提醒喵喵主人檢查喵喵身體：
```
example: 不管，這就是一個範例喵～
- By Emoji, ver. 1.0.0
- ❌ Error During Load Time
```
基於Telethon特性，如果在運行期間（例如執行指令期間）出錯，只會在主控臺丟出錯誤信息，而不會中斷程序或者給予使用者任何異常反饋，所以要監看主控臺看看有沒有喵喵在撒嬌或者哀嚎。
### 版權問題
由於主程序使用了高傳染性的GPL，所以所有插件都會被傳染GPL，戴口罩也沒有用喵～
### 結語
到底我他媽的幹嘛要在文檔上買萌啊喵？
