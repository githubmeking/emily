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
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Config import *

from ..database import dbsud, lang_set
from ..languages import get_str, lan
from ..languages.ALL import CHOICE_LANG, LANGAUGE
from .helpers import check_admin_and_edit, reload, cbblock, block
from .ping import ping


@Client.on_callback_query(filters.regex("cb_commands"))
@cbblock
async def cb_commands(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    if await dbsud.is_sudo_exist(query.from_user.id) is True:
        await query.edit_message_text(
            text=LAN.COMMANDS_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            LAN.TAGGER_COMMANDS, callback_data="tagger_commands"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.SETTINGS_COMMANDS, callback_data="settings_commands"
                        ),
                        InlineKeyboardButton(
                            LAN.ADDON_COMMANDS, callback_data="plus_commands"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.SUDOS_COMMANDS, callback_data="sudo_commands"
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
        await query.edit_message_text(
            text=LAN.COMMANDS_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            LAN.TAGGER_COMMANDS, callback_data="tagger_commands"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.SETTINGS_COMMANDS, callback_data="settings_commands"
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


@Client.on_callback_query(filters.regex("tagger_commands"))
@cbblock
async def tagger_commands(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.TAGGER_COMMANDS_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("plus_commands"))
@cbblock
async def plus_commands(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.ADDONS_COMMANDS_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("settings_commands"))
@cbblock
async def settings_commands(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.SETTINGS_COMMANDS_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("stop_tag"))
@cbblock
async def stop_tag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.STOPPED_COMMANDS_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("sudo_commands"))
@cbblock
async def sudo_commands(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.OWNER_HELP,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_info"))
@cbblock
async def cb_info(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_INFO,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_tag"))
@cbblock
async def cb_tag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_TAG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_aatag"))
@cbblock
async def cb_atag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_ATAG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_ctag"))
@cbblock
async def cb_ctag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_CTAG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_etag"))
@cbblock
async def cb_etag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_ETAG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_itag"))
@cbblock
async def cb_itag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_ITAG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_stag"))
@cbblock
async def cb_stag(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_STAG,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_cancel"))
@cbblock
async def cb_cancel(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await query.edit_message_text(
        text=LAN.HELP_CANCEL,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.GERI, callback_data="cb_commands"),
                ],
            ],
        ),
    )


@Client.on_callback_query(filters.regex("cb_start"))
@cbblock
async def cb_start(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    if query.from_user.id != OWNER_ID:
        await query.edit_message_text(
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
    else:
        await query.edit_message_text(
            text=LAN.STARTMSG.format(BOT_NAME),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(LAN.KOMUTLAR, callback_data="cb_commands"),
                    ],
                    [
                        InlineKeyboardButton(
                            LAN.SAHIP_KOMUTLAR, callback_data="owner_commands"
                        ),
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


@Client.on_callback_query(filters.regex("admins"))
@cbblock
async def cb_admins(bot: Client, query: CallbackQuery):
    await check_admin_and_edit(bot, query)


@Client.on_callback_query(filters.regex("ping"))
@cbblock
async def cb_ping(bot: Client, query: CallbackQuery):
    await ping(bot, query)


@Client.on_callback_query(filters.regex("cb_lang"))
@cbblock
async def cb_lang(bot: Client, query: CallbackQuery):
    chat = query.message.chat.id
    lang = await get_str(chat)
    LAN = lan(lang)
    global admins
    if query.message.chat.type == ChatType.PRIVATE:
        await query.message.edit(
            CHOICE_LANG,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🇹🇷 Türkçe", callback_data="lang_tr"),
                    ],
                    [
                        InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
                        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🇦🇿 Azərbaycanca", callback_data="lang_az"
                        ),
                    ],
                    [
                        InlineKeyboardButton(LAN.ANA_MENU, callback_data="cb_start"),
                    ],
                ],
            ),
        )
    else:
        await reload(bot, query.message, query.from_user.id)
        if query.from_user.id not in admins[query.message.chat.id]:
            return await query.answer(
                text=LAN.U_NOT_ADMIN.format(query.from_user.first_name), show_alert=True
            )
        else:
            await query.message.edit(
                CHOICE_LANG,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🇹🇷 Türkçe", callback_data="lang_tr"),
                            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
                        ],
                        [
                            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
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


@Client.on_callback_query(filters.regex("cb_del"))
@cbblock
async def cb_del(bot: Client, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("lang_tr"))
@cbblock
async def cb_lang_tr(bot: Client, query: CallbackQuery):
    lang = await get_str(query.message.chat.id)
    LAN = lan(lang)
    if query.message.chat.type == ChatType.PRIVATE:
        await lang_set(query.message.chat.id, "TR")
        await query.message.edit(
            text="Diliniz başarıyla Türkçe'ye değiştirildi",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(LAN.GERI, callback_data="cb_start"),
                    ]
                ]
            ),
        )
    else:
        await reload(bot, query.message, query.from_user.id)
        if query.from_user.id not in admins[query.message.chat.id]:
            return await query.answer(
                text=LAN.U_NOT_ADMIN.format(query.from_user.first_name), show_alert=True
            )
        else:
            await lang_set(query.message.chat.id, "TR")
            await query.message.edit(
                text="Diliniz başarıyla Türkçe'ye değiştirildi",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(LAN.GERI, callback_data="cb_settings"),
                        ]
                    ]
                ),
            )


@Client.on_callback_query(filters.regex("lang_en"))
@cbblock
async def cb_lang_en(bot: Client, query: CallbackQuery):
    lang = await get_str(query.message.chat.id)
    LAN = lan(lang)
    if query.message.chat.type == ChatType.PRIVATE:
        await lang_set(query.message.chat.id, "EN")
        await query.message.edit(
            text="Your language has been successfully changed to English",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(LAN.GERI, callback_data="cb_start"),
                    ]
                ]
            ),
        )
    else:
        await reload(bot, query.message, query.from_user.id)
        if query.from_user.id not in admins[query.message.chat.id]:
            return await query.answer(
                text=LAN.U_NOT_ADMIN.format(query.from_user.first_name), show_alert=True
            )
        else:
            await lang_set(query.message.chat.id, "EN")
            await query.message.edit(
                text="Your language has been successfully changed to English",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(LAN.GERI, callback_data="cb_settings"),
                        ]
                    ]
                ),
            )


@Client.on_callback_query(filters.regex("lang_ru"))
@cbblock
async def cb_lang_ru(bot: Client, query: CallbackQuery):
    lang = await get_str(query.message.chat.id)
    LAN = lan(lang)
    if query.message.chat.type == ChatType.PRIVATE:
        await lang_set(query.message.chat.id, "RU")
        await query.message.edit(
            text="Ваш язык успешно изменён на русский",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(LAN.GERI, callback_data="cb_start"),
                    ]
                ]
            ),
        )
    else:
        await reload(bot, query.message, query.from_user.id)
        if query.from_user.id not in admins[query.message.chat.id]:
            return await query.answer(
                text=LAN.U_NOT_ADMIN.format(query.from_user.first_name), show_alert=True
            )
        else:
            await lang_set(query.message.chat.id, "RU")
            await query.message.edit(
                text="Ваш язык успешно изменён на русский",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(LAN.GERI, callback_data="cb_settings"),
                        ]
                    ]
                ),
            )


@Client.on_callback_query(filters.regex("lang_az"))
@cbblock
async def cb_lang_az(bot: Client, query: CallbackQuery):
    lang = await get_str(query.message.chat.id)
    LAN = lan(lang)
    if query.message.chat.type == ChatType.PRIVATE:
        await lang_set(query.message.chat.id, "AZ")
        await query.message.edit(
            text="Diliniz Azərbaycan dilinə uğurla dəyişdirildi",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(LAN.GERI, callback_data="cb_start"),
                    ]
                ]
            ),
        )
    else:
        await reload(bot, query.message, query.from_user.id)
        if query.from_user.id not in admins[query.message.chat.id]:
            return await query.answer(
                text=LAN.U_NOT_ADMIN.format(query.from_user.first_name), show_alert=True
            )
        else:
            await lang_set(query.message.chat.id, "AZ")
            await query.message.edit(
                text="Diliniz Azərbaycan dilinə uğurla dəyişdirildi",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(LAN.GERI, callback_data="cb_settings"),
                        ]
                    ]
                ),
            )
