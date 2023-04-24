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


from pyrogram import Client, filters
from pyrogram.enums import *
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Config import *

from ..database import (
    delcmd_is_on,
    delcmd_off,
    delcmd_on,
    get_count,
    get_duration,
    set_count,
    set_duration,
)
from ..languages import get_str, lan
from ..languages.ALL import LANGAUGE
from .helpers import admin, clean_mode, command, reload


@Client.on_message(command(commands=["settings", "config"]))
@admin
async def settings(client: Client, message: Message):
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, message, message.from_user.id)
    if message.chat.type == ChatType.PRIVATE:
        return  # TODO
    if message.from_user.id not in admins[message.chat.id]:
        ms = await message.reply_text(LAN.U_NOT_ADMIN.format(message.from_user.mention))
        await clean_mode(message.chat.id, ms, message)
    else:
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LANGAUGE, callback_data="cb_lang"),
                    InlineKeyboardButton(LAN.COUNT_TEXT, callback_data="cb_count"),
                ],
                [
                    InlineKeyboardButton(LAN.DURATION_TEXT, callback_data="cb_dration"),
                    InlineKeyboardButton("Clean Modu #TODO", callback_data="cb_clean"),
                    # TODO clean mode yap
                ],
            ]
        )
        await clean_mode(message.chat.id, message)
        await message.reply_text(LAN.CHOICE_SET, reply_markup=buttons)


@Client.on_callback_query(filters.regex("cb_count"))
async def cb_count(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    query.from_user.id
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return  # TODO
    if query.from_user.id not in admins[query.message.chat.id]:
        return await query.answer(
            LAN.U_NOT_ADMIN.format(query.from_user.mention), show_alert=True
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("3", callback_data="count 3"),
                InlineKeyboardButton("4", callback_data="count 4"),
            ],
            [
                InlineKeyboardButton("5", callback_data="count 5"),
                InlineKeyboardButton("6", callback_data="count 6"),
            ],
            [
                InlineKeyboardButton("Geri", callback_data="cb_settings"),
            ],
        ]
    )
    deger = await get_count(chat_id)
    await query.message.edit_text(
        LAN.CHOICE_COUNT_NUMB.format(deger),
        reply_markup=buttons,
    )


@Client.on_callback_query(filters.regex("cb_dration"))
async def cb_dration(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    query.from_user.id
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return
    if query.from_user.id not in admins[query.message.chat.id]:
        return await query.answer(
            LAN.U_NOT_ADMIN.format(query.from_user.mention), show_alert=True
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("3 sn", callback_data="duration 3"),
                InlineKeyboardButton("4 sn", callback_data="duration 4"),
            ],
            [
                InlineKeyboardButton("5 sn", callback_data="duration 7"),
                InlineKeyboardButton("6 sn", callback_data="duration 6"),
            ],
            [
                InlineKeyboardButton("Geri", callback_data="cb_settings"),
            ],
        ]
    )
    await query.message.edit_text(
        LAN.CHOICE_DURATION_NUMB.format(await get_duration(chat_id)),
        reply_markup=buttons,
    )


@Client.on_message(command(commands=["count"]))
@admin
async def command_count(client: Client, message: Message):
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, message.from_user.id)
    if message.chat.type == ChatType.PRIVATE:
        return
    if message.from_user.id not in admins[message.chat.id]:
        return await message.reply_text(
            LAN.U_NOT_ADMIN.format(message.from_user.mention)
        )
    else:
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("3", callback_data="count 3"),
                    InlineKeyboardButton("4", callback_data="count 4"),
                ],
                [
                    InlineKeyboardButton("5", callback_data="count 5"),
                    InlineKeyboardButton("6", callback_data="count 6"),
                ],
            ]
        )
        deger = await get_count(chat_id)
        await message.reply_text(
            LAN.CHOICE_COUNT_NUMB.format(deger),
            reply_markup=buttons,
        )


@Client.on_message(command(commands=["duration"]))
@admin
async def command_duration(client: Client, message: Message):
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, message.from_user.id)
    if message.chat.type == ChatType.PRIVATE:
        return
    if message.from_user.id not in admins[message.chat.id]:
        return await message.reply_text(
            LAN.U_NOT_ADMIN.format(message.from_user.mention)
        )
    else:
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("3", callback_data="duration 3"),
                    InlineKeyboardButton("4", callback_data="duration 4"),
                ],
                [
                    InlineKeyboardButton("5", callback_data="duration 5"),
                    InlineKeyboardButton("6", callback_data="duration 6"),
                ],
            ]
        )
        deger = await get_duration(chat_id)
        await message.reply_text(
            LAN.CHOICE_DURATION_NUMB.format(deger),
            reply_markup=buttons,
        )


@Client.on_callback_query(filters.regex(r"count"))
async def countt(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    count = int(query.data.split(" ")[1])
    user_id = query.from_user.id
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return
    if user_id not in admins[query.message.chat.id]:
        return await query.answer(
            LAN.U_NOT_ADMIN.format(query.from_user.mention), show_alert=True
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    else:
        await set_count(chat_id, count)
        await query.message.edit(
            LAN.CHANGED_COUNT.format(count),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(LAN.GERI, callback_data="cb_settings")]]
            ),
        )


@Client.on_callback_query(filters.regex(r"duration"))
async def duration(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    duration = query.data.split(" ")[1]
    user_id = query.from_user.id
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return
    if user_id not in admins[query.message.chat.id]:
        return await query.answer(
            LAN.U_NOT_ADMIN.format(query.from_user.mention), show_alert=True
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    else:
        await set_duration(chat_id, duration)
        await query.message.edit(
            LAN.CHANGED_DURATION.format(duration),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Geri", callback_data="cb_settings")]]
            ),
        )


@Client.on_callback_query(filters.regex("cb_clean"))
async def clean(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    query.from_user.id
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return  # TODO
    if query.from_user.id not in admins[query.message.chat.id]:
        return await query.answer(
            LAN.U_NOT_ADMIN.format(query.from_user.mention), show_alert=True
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Açık", callback_data="clean 1"),
                InlineKeyboardButton("Kapalı", callback_data="clean 0"),
            ],
            [
                InlineKeyboardButton("Geri", callback_data="cb_settings"),
            ],
        ]
    )
    if await delcmd_is_on(chat_id) is True:
        deger = "✅"
    else:
        deger = "❌"
    await query.message.edit_text(
        "Mevcut Değer: ".format(deger),
        reply_markup=buttons,
    )


@Client.on_callback_query(filters.regex(r"clean"))
async def cb_clean(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    clean_mode = query.data.split(" ")[1]
    user_id = query.from_user.id
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return
    if user_id not in admins[query.message.chat.id]:
        return await query.answer(
            LAN.U_NOT_ADMIN.format(query.from_user.mention), show_alert=True
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    else:
        if clean_mode == "1":
            await delcmd_on(chat_id)
            await query.message.edit(
                "Açıldı",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Geri", callback_data="cb_settings")]]
                ),
            )
        elif clean_mode == "0":
            await delcmd_off(chat_id)
            await query.message.edit(
                "Açıldı",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Geri", callback_data="cb_settings")]]
                ),
            )


@Client.on_callback_query(filters.regex("cb_settings"))
async def cb_settings(client: Client, query: CallbackQuery):
    query.message.from_user.id
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, query.message.from_user.id)
    if query.message.chat.type == ChatType.PRIVATE:
        return  # TODO
    if query.message.from_user.id not in admins[query.message.chat.id]:
        return await query.message.edit(
            LAN.U_NOT_ADMIN.format(query.message.from_user.mention)
        )
    if ADMIN == "True" and BOT_ID[0] not in admins[query.message.chat.id]:
        return await query.message.edit(LAN.NEED_ADMIN)
    else:
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LANGAUGE, callback_data="cb_lang"),
                    InlineKeyboardButton(LAN.COUNT_TEXT, callback_data="cb_count"),
                ],
                [
                    InlineKeyboardButton(LAN.DURATION_TEXT, callback_data="cb_dration"),
                    InlineKeyboardButton("Clean Mode #TODO", callback_data="cb_clean"),
                ],
                [
                    InlineKeyboardButton("❌", callback_data="cb_del"),
                ],
            ]
        )
        await query.message.edit(LAN.CHOICE_SET, reply_markup=buttons)
