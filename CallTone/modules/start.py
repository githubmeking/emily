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
from asyncio.exceptions import CancelledError

from pyrogram import Client, filters
from pyrogram.enums import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Config import *

from ..database import lang_set
from ..languages import CallTone_AZ, CallTone_EN, CallTone_RU, CallTone_TR, get_str, lan
from ..languages.ALL import CHOICE_LANG, LANGAUGE
from .helpers import FILE_CONTROL, command, reload, block


@Client.on_message(command("restart") & filters.user(OWNER_ID))
async def resart_(bot, msg: Message):
    a = await msg.reply(
        f"__Bot yeniden başlatılmaya çalışılacak, lütfen terminali kontrol edin...__"
    )
    file = FILE_CONTROL(file_name="LAST_RESTART_MESSAGE")
    return_ = file.set(f"{a.chat.id}|{a.id}")
    print(return_)
    try:
        import sys
        from os import environ, execle

        args = [sys.executable, "-m", "CallTone"]

        execle(sys.executable, *args, environ)
    except CancelledError:
        print(0)
    except Exception as e:
        print(e)


@Client.on_message(command("shutdown") & filters.user(OWNER_ID))
async def resart_(bot, msg: Message):
    a = await msg.reply(
        f"**Bot kapatalıyor. Tekrar manuel açabilirsiniz.**"
    )

    try:
        import sys
        from os import environ, execle

        args = [sys.executable, "print('Bot Kapatıldı')", ]

        execle(sys.executable, *args, environ)

    except CancelledError:
        print(0)
    except Exception as e:
        print(e)


@Client.on_message(command("start") & filters.private)
@block
async def start(bot: Client, msg: Message):
    chat_id = msg.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    if len(msg.command) == 1:
        await bot.send_message(
            msg.chat.id,
            text=LAN.STARTMSG.format(BOT_NAME),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(LAN.KOMUTLAR, callback_data="cb_commands"),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.GRUBAEKLE,
                            url=f"https://t.me/{BOT_USERNAME}?startgroup=a",
                        ),
                        InlineKeyboardButton(LAN.SAHIBIM, user_id=OWNER_ID),
                    ],
                    [InlineKeyboardButton(LANGAUGE, callback_data="cb_lang")],
                ],
            ),
        )
    elif len(msg.command) >= 2:
        query = msg.command[1]
        if query.startswith("help"):
            if msg.chat.type == ChatType.PRIVATE:
                await bot.send_message(
                    chat_id=msg.chat.id,
                    text=LAN.HELPMSG.format(BOT_USERNAME),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    LAN.KOMUTLAR, callback_data="cb_commands"
                                ),
                                InlineKeyboardButton(
                                    LAN.YARDIM, url=f"https://t.me/{GROUP_SUPPORT}"
                                ),
                            ],
                        ],
                    ),
                    disable_web_page_preview=True,
                )


@Client.on_message(command("help"))
@block
async def help(bot: Client, msg: Message):
    chat_id = msg.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    if msg.chat.type == ChatType.PRIVATE:
        await bot.send_message(
            chat_id=msg.chat.id,
            text=LAN.COMMANDS_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            LAN.TAGGER_COMMANDS, callback_data="tag_commands"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.SETTINGS_COMMANDS, url="settings_commands"
                        ),
                        InlineKeyboardButton(
                            LAN.ADDON_COMMANDS, callback_data="plus_commands"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.STOPPED_COMMANDS, callback_data="stop_tag"
                        ),
                    ],
                ],
            ),
            disable_web_page_preview=True,
        )
    else:
        await msg.reply(
            LAN.YARDIM_BUTONU,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            LAN.TIKLA, url=f"https://t.me/{BOT_USERNAME}?start=help"
                        ),
                    ],
                ],
            ),
        )


@Client.on_message(command("lang"))
@block
async def lang(bot: Client, msg: Message):
    chat_id = msg.chat.id
    lang = await get_str(chat_id)
    langs = ["TR", "EN", "RU", "AZ"]
    LAN = lan(lang)
    if msg.chat.type == ChatType.PRIVATE:
        if len(msg.command) == 2:
            langg = msg.command[1]
            if langg.upper() in langs:
                await lang_set(chat_id, langg.upper())
                await bot.send_message(
                    chat_id=msg.chat.id,
                    text=LAN.LANG_SET.format(langg.upper()),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("❌", callback_data="cb_del"),
                            ],
                        ],
                    ),
                )
            else:
                await bot.send_message(
                    chat_id=msg.chat.id,
                    text=CHOICE_LANG,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "🇹🇷 Türkçe", callback_data="lang_tr"
                                ),
                                InlineKeyboardButton(
                                    "🇬🇧 English", callback_data="lang_en"
                                ),
                            ],
                            [
                                InlineKeyboardButton(
                                    "🇷🇺 Русский", callback_data="lang_ru"
                                ),
                                InlineKeyboardButton(
                                    "🇦🇿 Azərbaycanca", callback_data="lang_az"
                                ),
                            ],
                            [
                                InlineKeyboardButton("🗑", callback_data="cb_del"),
                            ],
                        ],
                    ),
                )
    else:
        await reload(bot, msg, msg.from_user.id)
        if msg.from_user.id not in admins[msg.chat.id]:
            return await msg.reply(
                text=LAN.U_NOT_ADMIN.format(msg.from_user.first_name)
            )
        else:
            if len(msg.command) == 2:
                langg = msg.command[1]
                langgg = langg.upper()
                if langgg in langs:
                    await lang_set(chat_id, langgg)
                    if langgg == "TR":
                        text = CallTone_TR.LANG_SET
                    elif langgg == "EN":
                        text = CallTone_EN.LANG_SET
                    elif langgg == "RU":
                        text = CallTone_RU.LANG_SET
                    elif langgg == "AZ":
                        text = CallTone_AZ.LANG_SET
                    c = await bot.send_message(chat_id=msg.chat.id, text=text)
                    await sleep(5)
                    await c.delete()
                else:
                    await bot.send_message(
                        chat_id=msg.chat.id,
                        text=CHOICE_LANG,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "🇹🇷 Türkçe", callback_data="lang_tr"
                                    ),
                                    InlineKeyboardButton(
                                        "🇬🇧 English", callback_data="lang_en"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton(
                                        "🇷🇺 Русский", callback_data="lang_ru"
                                    ),
                                    InlineKeyboardButton(
                                        "🇦🇿 Azərbaycanca", callback_data="lang_az"
                                    ),
                                ],
                                [
                                    InlineKeyboardButton("🗑", callback_data="cb_del"),
                                ],
                            ],
                        ),
                    )
            else:
                await bot.send_message(
                    chat_id=msg.chat.id,
                    text=CHOICE_LANG,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "🇹🇷 Türkçe", callback_data="lang_tr"
                                ),
                                InlineKeyboardButton(
                                    "🇬🇧 English", callback_data="lang_en"
                                ),
                            ],
                            [
                                InlineKeyboardButton(
                                    "🇷🇺 Русский", callback_data="lang_ru"
                                ),
                                InlineKeyboardButton(
                                    "🇦🇿 Azərbaycanca", callback_data="lang_az"
                                ),
                            ],
                            [
                                InlineKeyboardButton("🗑", callback_data="cb_del"),
                            ],
                        ],
                    ),
                )


@Client.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    #print(BOT_ID[0])
    lang = await get_str(msg.chat.id)
    LAN = lan(lang)
    for new_user in msg.new_chat_members:
        if new_user.id == BOT_ID[0]:
            await msg.reply(
                LAN.WELCOME_TEXT,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                LAN.TIKLA, url=f"https://t.me/{BOT_USERNAME}?start=help"
                            ),
                        ],
                    ],
                ),
            )

        elif new_user.id == OWNER_ID:
            await msg.reply(LAN.OWNER_WELCOME)
