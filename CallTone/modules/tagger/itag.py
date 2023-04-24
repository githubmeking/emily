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

from random import choice

from pyrogram import Client
from pyrogram.enums import *
from pyrogram.types import Message
from Config import BANNED_CHATS, BANNED_USERS
from ...languages import get_str, lan
from ..helpers import admin, command, emojiler, extract_user, reload, block, cbblock


@Client.on_message(command(["itag"]) &~BANNED_CHATS &~BANNED_USERS)
@admin
@block
async def itag(client: Client, message: Message):
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, message, message.from_user.id)
    if message.chat.type == ChatType.PRIVATE:
        return
    try:
        await message.delete()
    except BaseException:
        pass
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == message.chat.id:
            return await message.reply(LAN.CANT_TAG_ANONIM)
        else:
            user_id = message.reply_to_message.from_user.id
    else:
        user_id, _ = extract_user(message)
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await message.reply(LAN.NO_USER)
        await client.send_message(
            chat_id, f"[{choice(emojiler)}](tg://user?id={user.id})"
        )
