# -*- coding: utf-8 -*-

# (c) @aylak-github (Github) | https://t.me/ayIak | @BasicBots (Telegram)

#==============================================================================
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
#==============================================================================
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
#========================================================================

from datetime import datetime

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ..languages import get_str, lan
from .helpers import clean_mode, command, block
from Config import BANNED_CHATS, BANNED_USERS

@Client.on_message(command("ping") &~BANNED_CHATS &~BANNED_USERS)
@block
async def pingy(client, message):

    start = datetime.now()
    hmm = await message.reply("`Pong!`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await clean_mode(message.chat.id, message)
    await hmm.edit(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(f"Ping!: {round(ms)}ms", callback_data="ping")],
            ],
        ),
    )


async def ping(bot, query):
    start = datetime.now()
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await bot.answer_callback_query(
        callback_query_id=query.id, text=LAN.PING_CB_TEXT, show_alert=True
    )
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await query.edit_message_text(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"Ping!: {round(ms)}ms", callback_data="ping")]]
        ),
    )
