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

from asyncio import sleep
from random import choice

from pyrogram import Client, filters
from pyrogram.enums import *
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Config import *

from ...database import get_count, get_duration
from ...languages import get_str, lan
from ..helpers import admin, clean_mode, count, reload, sozler, block, cbblock


@Client.on_message(filters.command(commands="stag", prefixes=COMMAND))
@admin
@block
async def ptag(client: Client, message: Message):
    global calisan
    global reasons
    global admins
    chat_id = message.chat.id
    user_id = message.from_user.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, message, message.from_user.id)

    if message.chat.type == ChatType.PRIVATE:
        return

    if message.from_user.id not in admins[message.chat.id]:
        not_admin = await message.reply_text(
            LAN.U_NOT_ADMIN.format(message.from_user.mention)
        )
        await clean_mode(message.chat.id, not_admin, message)
        return

    if chat_id in calisan:
        c = await message.reply_text(
            LAN.ZATEN_CALISIYORUM.format(message.from_user.mention)
        )
        await clean_mode(message.chat.id, c, message)
        return

    else:
        if message.reply_to_message:
            if message.reply_to_message.text:
                reason = message.reply_to_message.text
                tip = "1"
            else:
                reason = ""
                tip = "0"
        else:
            if len(message.command) <= 1:
                reason = ""
                tip = "0"
            else:
                reason = message.text.split(None, 1)[1]
                tip = "1"
        COUNT = await get_count(chat_id)
        reasons[chat_id] = reason
        m = await client.send_message(
            chat_id,
            LAN.ASK_SOZ_TAG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            LAN.TEKLI, callback_data=f"ptag 1|{user_id}|{tip}"
                        ),
                        InlineKeyboardButton(
                            LAN.COKLU.format(COUNT),
                            callback_data=f"ptag {COUNT}|{user_id}|{tip}",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "❌", callback_data=f"ptag 0|{user_id}|{tip}"
                        ),
                    ],
                ],
            ),
        )
        await sleep(15)
        if chat_id not in calisan:
            try:
                await m.edit(
                    LAN.ASK_ADMINS_TAG_TIMEOUT.format(
                        message.from_user.mention, "`/atag`"
                    )
                )
            except Exception:
                return
            await clean_mode(message.chat.id, m, message)
            return
        else:
            return


@Client.on_callback_query(filters.regex(pattern=r"ptag"))
@cbblock
async def pcommands(bot: Client, query: CallbackQuery):
    global admins
    global reasons
    global calisan
    q = query.data
    chat = int(query.message.chat.id)
    lang = await get_str(chat)
    LAN = lan(lang)
    DURATION = await get_duration(chat)
    typed_ = str(q).split()[1]
    sayi = int(typed_.split("|")[0])
    useer_id = typed_.split("|")[1]
    tip = typed_.split("|")[2]

    if sayi == 0:
        del reasons[chat]
        await query.message.edit_text(
            LAN.CALISMA_DURDUR.format(query.from_user.mention)
        )
        await sleep(DURATION)
        await query.message.delete()
        return

    if chat in calisan:
        await query.message.edit(
            LAN.ZATEN_CALISIYORUM.format(query.message.from_user.mention)
        )
        await clean_mode(query.message.chat.id, query.message)
        return

    if tip == "1":
        reason = reasons[chat]
    elif tip == "0":
        reason = ""

    name = await bot.get_users(int(useer_id))
    if int(useer_id) == int(query.from_user.id):
        if chat not in calisan:
            calisan.append(chat)
        await query.message.delete()
        bots, deleted, toplam = await count(bot, chat)
        etiketlenecek = toplam - (bots + deleted)
        started = await bot.send_message(
            chat,
            LAN.TAG_START.format(
                query.from_user.mention, "Sözle Etiketleme", etiketlenecek, DURATION
            ),
        )
        usrnum = 0
        usrtxt = ""
        etiketlenen = 0
        async for usr in bot.get_chat_members(chat):
            if usr.user.is_bot:
                pass
            elif usr.user.is_deleted:
                pass
            else:
                emoji = choice(sozler)
                usrnum += 1
                usrtxt += f"[{emoji}](tg://user?id={usr.user.id}) ,"
                etiketlenen += 1

                if usrnum == int(sayi):
                    if sayi == 1:
                        text = f"📢 **{reason}** {usrtxt}"
                    else:
                        text = f"📢 **{reason}**\n\n{usrtxt}"
                    await bot.send_message(chat, text=text)
                    await sleep(DURATION)
                    usrnum = 0
                    usrtxt = ""

                if etiketlenen == etiketlenecek:
                    calisan.remove(chat)
                    del reasons[chat]
                    stoped = await bot.send_message(
                        chat,
                        LAN.TAG_STOPED.format(
                            "Sözle Etiketleme",
                            etiketlenen,
                            DURATION,
                            query.from_user.mention,
                        ),
                    )
                    await clean_mode(query.message.chat.id, started, stoped)
                    return

                if chat not in calisan:
                    del reasons[chat]
                    stopped = await bot.send_message(
                        chat,
                        LAN.TAG_STOPED.format(
                            "Sözle Etiketleme",
                            etiketlenen,
                            DURATION,
                            query.from_user.mention,
                        ),
                    )
                    await clean_mode(query.message.chat.id, started, stopped)
                    return
    else:
        return await bot.answer_callback_query(
            callback_query_id=query.id,
            text=LAN.ETAG_DONT_U.format(name.first_name),
            show_alert=True,
        )
