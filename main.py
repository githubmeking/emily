# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# Tüm hakları saklıdır.
#
# Bu dosya, < https://github.com/aylak-github/CallTone > parçasıdır.
# Lütfen GNU Affero Genel Kamu Lisansını okuyun;
# < https://www.github.com/aylak-github/CallTone/blob/master/LICENSE/ >
# ================================================================


import logging
from logging import INFO
import sys
from pyrogram import Client, filters, idle, __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from tglogging import TelegramLogHandler

from Config import *

# TGLOGGING Uygulamanızın logunu Telegram'a anlık göndermenizi sağlar. 

logging.basicConfig(
    level=INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        TelegramLogHandler(
            token=BOT_TOKEN, 
            log_chat_id=LOG_CHANNEL, 
            update_interval=2, 
            minimum_lines=1, # Her Mesajda gönderilecek satır sayısı
            pending_logs=200000),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("CallTone Bot Logger")

logger.info("Telegram'a canlı log başlatıldı.")

app = Client(
    "CallTone",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="modules"),
)



app.storage.SESSION_STRING_FORMAT = ">B?256sQ?"


if __name__ == "__main__":
    app.start()
    uname = app.get_me().username
    try:
        app.send_message(LOG_CHANNEL, f"**@{uname} başarıyla başlatıldı! Hatalar, eksikler, öneriler ve geri kalan her şey için destek grubuna gelin!**\n\n__By @meftrah - @sohbet1numara__", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Destek Grubu", url="https://t.me/destekgroup")]]))
    except Exception:
        print(f"Log grubuna ( {LOG_CHANNEL} ) erişim sağlanamadı. Lütfen botu gruba alıp tam yetki verin. Botun kullanıcı adı: @{uname}. İşlem durduruluyor...")
        app.stop() # Stop the bot
        app2.stop() 
        sys.exit(1) # Programı durdurur.
    print(f"@{uname}, {__version__} pyrogram sürümü ile başlatıldı!")

    idle()

    app.stop()
    print(f"@{uname} durduruldu!")
