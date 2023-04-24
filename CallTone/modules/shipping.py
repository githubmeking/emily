# -*- coding: utf-8 -*-

# (c) @aylak-github (Github) | https://t.me/ayIak | @BasicBots (Telegram)

# ==============================================================================
#
# Project: CallToneBot
# Copyright (C) 2021-2022 by aylak-github@Github, < https://github.com/aylak-github >.
#
# This file is part of < https://github.com/aylak-github/CallTone > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/aylak-github/CallTone/blob/master/LICENSE >
#
# All rights reserved.
#
# ==============================================================================
#
# Proje: CallToneBot
# Telif Hakkı (C) 2021-2022 aylak-Github@Github, <https://github.com/aylak-github>.
#
# Bu dosya <https://github.com/aylak-github/CallTone> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. < https://github.com/aylak-github/CallTone/blob/master/LICENSE >
#
# Her hakkı saklıdır.
#
# ========================================================================


import random

from pyrogram import Client, filters
from pyrogram.types import ChatMember, Message

from ..languages import get_str, lan
from .helpers import admin, clean_mode, command, block
from Config import BANNED_CHATS, BANNED_USERS

kalpler = "🧡 💛 💚 💙 💜 🤎 🖤 🤍 💔 💔 💔 ❣ 💕 💞 💓 💓 💗 💖 💘 💝".split()


new_users_dict = {}


@Client.on_message(command(["eros", "ship"]) & ~filters.private & ~BANNED_CHATS & ~BANNED_USERS)
@admin
@block
async def ship(client: Client, message: Message):
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    mentions = ""
    users_list = {}
    if chat_id not in new_users_dict:
        print("Yeni bir sohbet için kullanıcılar listeleniyor...")
        async for mentions in client.get_chat_members(message.chat.id):
            mentions: ChatMember
            if mentions.user.is_bot:
                continue
            if mentions.user.is_deleted:
                continue
            else:
                users_list.update(
                    {
                        mentions.user.id: dict(
                            first_name=mentions.user.first_name,
                            status=mentions.status,
                            username=mentions.user.username,
                        )
                    }
                )
        
        new_users_dict[chat_id] = users_list
    else:
        print("Sohbet için kullanıcılar listeleniyor...")
        users_list = new_users_dict[chat_id]

    if len(users_list) < 2:
        return
    m1_id = random.choice(list(users_list.keys()))
    m2_id = random.choice(list(users_list.keys()))
    oran = random.randint(1, 100)
    kalp = random.choice(kalpler)
    while m1_id == m2_id:
        m1_id = random.choice(list(users_list.keys()))
    if users_list[m1_id]["status"] == "creator":
        mention1 = f"👑 [{users_list[m1_id]['first_name']}](tg://user?id={m1_id}) 👑"
    elif users_list[m2_id]["status"] == "creator":
        mention2 = f"👑 [{users_list[m2_id]['first_name']}](tg://user?id={m2_id}) 👑"
    else:
        mention1 = f"[{users_list[m1_id]['first_name']}](tg://user?id={m1_id})"
        mention2 = f"[{users_list[m2_id]['first_name']}](tg://user?id={m2_id})"

    if (
        users_list[m1_id]["status"] == "creator"
        or users_list[m1_id]["status"] == "creator"
    ):
        ship_text = LAN.SHIP_ADMIN
        oran = 100
        durum = 1
    elif oran <= 20:
        ship_text = LAN.SHIP_TEXT_1
        durum = 2
    elif oran <= 40:
        ship_text = LAN.SHIP_TEXT_2
        durum = 3
    elif oran <= 60:
        ship_text = LAN.SHIP_TEXT_3
        durum = 4
    elif oran <= 80:
        ship_text = LAN.SHIP_TEXT_4
        durum = 5
    else:
        ship_text = LAN.SHIP_TEXT_5
        durum = 6

    if durum == 1:
        h = ship_text.format(mention1, mention2)
    elif durum == 2:
        h = ship_text.format(mention1, mention2, oran)
    elif durum == 3:
        h = ship_text.format(mention1, kalp, mention2, oran)
    elif durum == 4:
        h = ship_text.format(mention1, kalp, mention2, oran)
    elif durum == 5:
        h = ship_text.format(mention1, kalp, mention2, oran)
    elif durum == 6:
        h = ship_text.format(mention1, kalp, mention2, oran)
    await client.send_message(message.chat.id, h)
    await clean_mode(message.chat.id, message)
