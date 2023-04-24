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


import asyncio
from datetime import datetime
import os
import shutil
import traceback

import psutil
from pyrogram import Client, filters
from pyrogram.enums import *
from pyrogram.errors import FloodWait, PeerIdInvalid, UserIsBlocked, UserIsBot
from pyrogram.types import *

from Config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    LOG_CHANNEL,
    OWNER_ID,
    SUDOS,
    calisan,
    BANNED_CHATS,
    BANNED_USERS,
    bakim,
)

from ..database import CHATS, dbsud, keydb, USERS, BAKIM
from ..languages import get_str, lan
from .helpers import clean_mode, command, extract_user, humanbytes, is_int, cbsudo, sudo, block


@Client.on_message(
    command(["allsudo", "listsudo", "sudolist", "sudolistesi", "sudoliste"])
    # & filters.user(SUDOS)
    & ~BANNED_CHATS
    & ~BANNED_USERS
)
@block
async def all_sudo(bot: Client, msg: Message):
    global SUDOS
    sudos = await dbsud.get_all_sudos()
    # print(sudos)
    #print(SUDOS)
    text = ""
    for user in sudos:
        # print(user, user['id'])
        try:
            usr = await bot.get_users(user["id"])
        except FloodWait as e:
            await asyncio.sleep(e.x)
            usr = await bot.get_users(user["id"])
        except PeerIdInvalid:
            await dbsud.delete_sudos(usr.id)
        except UserIsBlocked:
            await dbsud.delete_sudos(usr.id)
        except UserIsBot:
            await dbsud.delete_sudos(usr.id)
        if usr.first_name is None:
            await dbsud.delete_sudos(usr.id)
            continue
        text += f"**[{usr.first_name}](tg://user?id={usr.id})** [ `{usr.id}` ]\n"
    await bot.send_message(
        msg.chat.id,
        text=text,
    )

@Client.on_message(command(["bakim"]) & filters.user(OWNER_ID))
async def bakim_(bot: Client, msg: Message):
    bakims_ = BAKIM()
    if await bakims_.is_bakim():
        await bakims_.bakim_bitir()
        bakim.clear()
        bakim.append(True)
        
        await msg.reply_text("**Bakım modu kapatıldı.**")
    else:
        await bakims_.bakima_al()
        bakim.clear()
        bakim.append(False)
        
        await msg.reply_text("**Bakım modu açıldı.**")

# Log kanalını ayarlama komutu
@Client.on_message(command("setlog") & filters.user(OWNER_ID))
async def set_log(bot: Client, msg: Message):
    # global LOG_CHANNEL[0]
    if len(msg.command) >= 2:
        if is_int(msg.command[1]):
            await keydb.set(key="LOG_CHANNEL[0]", value=msg.command[1])
            LOG_CHANNEL[0] = int(msg.command[1])
            await msg.reply_text(f"Log kanalı başarıyla ayarlandı: {msg.command[1]}")
        else:
            await msg.reply_text("Kullanım: /setlog [kanal id]")
    else:
        await msg.reply_text("Kullanım: /setlog [kanal id]")


# Log kanalını silme komutu
@Client.on_message(command("dellog") & filters.user(OWNER_ID))
async def del_log(bot: Client, msg: Message):
    await keydb.del_(key="LOG_CHANNEL[0]")
    await msg.reply_text("**Log kanalı başarıyla silindi.**")


# Log kanalını gösterme komutu
@Client.on_message(command("log") & filters.user(OWNER_ID))
async def get_log(bot: Client, msg: Message):
    # global LOG_CHANNEL[0]
    log = LOG_CHANNEL[0]
    if log:
        await msg.reply_text(f"**Log Kanalı:** `{log}`")
    else:
        await msg.reply_text("**Log kanalı ayarlanmamış.**")


@Client.on_message(command("addsudo"))
async def add_sudo(bot: Client, msg: Message):
    if msg.from_user.id == OWNER_ID:
        if len(msg.command) >= 2 or msg.reply_to_message:
            user_id, user_first_name = extract_user(msg)
            try:
                user = await bot.get_users(user_id)
            except BaseException:
                await bot.send_message(msg.chat.id, "Kullanıcı bulunamadı.")
                return
            if await dbsud.is_sudo_exist(user.id):
                await bot.send_message(
                    msg.chat.id,
                    f"Bu kullanıcı [ [{user.first_name}](tg://user?id={user.id}) ] zaten sudo'ya eklenmiş.",
                )
            else:
                SUDOS.append(user.id)
                await dbsud.add_sudo(user.id)
                await bot.send_message(
                    msg.chat.id,
                    f"[{user.first_name}](tg://user?id={user.id})  sudo olarak eklendi.",
                )
        else:
            return await bot.send_message(
                msg.chat.id,
                "Kullanım: /addsudo [id/kullanıcı adı/mention/birinin mesajını yanıtlayarak]",
            )
    #   else:
    #       return await bot.send_message(
    #           msg.chat.id, "Bu komutu sadece sahibim kullanabilir."
    #       )


@Client.on_message(command("delsudo"))
async def delf_sudo(bot: Client, msg: Message):
    if msg.from_user.id == OWNER_ID:
        if len(msg.command) >= 2 or msg.reply_to_message:
            user_id, user_first_name = extract_user(msg)
            try:
                user = await bot.get_users(user_id)
            except BaseException:
                await bot.send_message(msg.chat.id, "Kullanıcı bulunamadı.")
                return
            if await dbsud.is_sudo_exist(user.id) is None:
                await bot.send_message(
                    msg.chat.id,
                    f"Bu kullanıcı [ [{user_first_name}](tg://user?id={user.id}) ] zaten sudo'ya eklenmemiş.",
                )
            else:
                SUDOS.remove(user.id)
                await dbsud.delete_sudos(user.id)
                await bot.send_message(
                    msg.chat.id,
                    f"[{user_first_name}](tg://user?id={user.id})  sudo olarak silindi.",
                )
        else:
            return await bot.send_message(
                msg.chat.id, "Kullanım: /delsudo [id/kullanıcı adı/mention]"
            )
    #   else:
    #       return await bot.send_message(
    #           msg.chat.id, "Bu komutu sadece sahibim kullanabilir."
    #       )


@Client.on_message(filters.command("block"))
@sudo
async def ban_user_chat(bot: Client, message: Message):
    user = message.from_user
    chat = message.chat
    lang = await get_str(chat.id)
    LAN = lan(lang)
    users = USERS()
    chats = CHATS()
    duration = "Sınırsız"
    if message.reply_to_message:
        user_id = str(message.reply_to_message.from_user.id)
    else:
        if len(message.command) <= 1:
            await message.reply_text(
                LAN.BAN_REASON_10.format(message.from_user.mention)
            )
            return
        user_id = message.command[1]

    if is_int(user_id) is False:
        await message.reply_text(LAN.BAN_REASON_10.format(message.from_user.mention))
        return

    if int(user_id) == OWNER_ID:
        await message.reply_text("Sahibimi yasaklayamam.")
        return
    if int(user_id) in SUDOS:
        await message.reply_text("Bu kullanıcı sudo olduğu için yasaklanamaz.")
        return

    list1 = await chats.blacklisted_chats()
    lisst2 = await users.blocked_users()

    if int(user_id) in lisst2 or int(chat.id) in list1:
        await message.reply_text("Bu kullanıcı/sohbet zaten yasaklanmış.")
        return

    if message.command[1].startswith("-"):
        error = LAN.BAN_REASON_2.format(
            user.mention, chat.id, duration, LAN.BAN_REASON_1.format(BOT_USERNAME)
        )
        await chats.blacklist_chat(int(user_id))
        text = LAN.BAN_REASON_3.format(LAN.BAN_REASON_1.format(BOT_USERNAME))
        try:
            await bot.send_message(int(user_id), text)
        except Exception as e:
            error += LAN.BAN_REASON_5.format(e)
        await bot.leave_chat(int(user_id))
        await message.reply_text(error)
        return
    else:
        error = LAN.BAN_REASON_6.format(
            user.mention, chat.id, duration, LAN.BAN_REASON_1.format(BOT_USERNAME)
        )
        await users.block_user(int(user_id))
        text = LAN.BAN_REASON_7.format(LAN.BAN_REASON_1.format(BOT_USERNAME))
        try:
            await bot.send_message(int(user_id), text)
        except Exception as e:
            error += LAN.BAN_REASON_9.format(e)
        await message.reply_text(error)
        return


@Client.on_message(filters.command("unblock"))
@sudo
async def unban_user_chat(bot: Client, message: Message):
    user = message.from_user
    chat = message.chat
    lang = await get_str(chat.id)
    LAN = lan(lang)
    users = USERS()
    chats = CHATS()
    if message.reply_to_message:
        user_id = str(message.reply_to_message.from_user.id)
    else:
        if len(message.command) <= 1:
            await message.reply_text(
                LAN.BAN_REASON_10.format(message.from_user.mention)
            )
            return
        user_id = message.command[1]
    if is_int(user_id) is False:
        await message.reply_text(LAN.BAN_REASON_10.format(message.from_user.mention))
        return

    list1 = await chats.blacklisted_chats()
    lisst2 = await users.blocked_users()()

    if int(user_id) not in lisst2 or int(chat.id) not in list1:
        await message.reply_text("Bu kullanıcı/sohbet zaten yasaklamanmış.")
        return

    if len(message.command) > 1:
        if message.command[1].startswith("-"):
            error = LAN.BAN_REASON_11.format(user.mention, chat.id)
            await chats.white_list_chat(int(user_id))
            text = LAN.BAN_REASON_12
            try:
                await bot.send_message(int(user_id), text)
            except Exception as e:
                error += LAN.BAN_REASON_5.format(e)
            await message.reply_text(error)
            return
    else:
        error = LAN.BAN_REASON_11.format(user.mention, message.from_user.id)
        await users.unblock_user(int(user_id))
        text = LAN.BAN_REASON_12
        try:
            await bot.send_message(int(user_id), text)
        except Exception as e:
            error += LAN.BAN_REASON_9.format(e)
        await message.reply_text(error)
        return


@Client.on_message(filters.command("blocklist"))
@sudo
async def ban_list(bot: Client, message: Message):

    user = message.from_user
    chat = message.chat
    lang = await get_str(chat.id)
    LAN = lan(lang)
    users = USERS()
    chats = CHATS()
    banned_usr_count = 0
    text = ""
    blockeds = await users.blocked_users()
    for banned_user in blockeds:
        user_id = banned_user
        #   ban_duration = banned_user["ban_status"]["ban_duration"]
        #   banned_on = banned_user["ban_status"]["banned_on"]
        #   ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BAN_REASON_13.format(
            user_id, "Sınırsız", "Bilinmiyor", "Belirtilmemiş"
        )
    for banned_chat in await chats.blacklisted_chats():
        chat_id = banned_chat
        #   ban_duration = banned_chat["ban_status"]["ban_duration"]
        #   banned_on = banned_chat["ban_status"]["banned_on"]
        #   ban_reason = banned_chat["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BAN_REASON_13.format(
            chat_id, "Sınırsız", "Bilinmiyor", "Belirtilmemiş"
        )
    reply_text = LAN.BAN_REASON_14.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await message.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await message.reply_text(reply_text)


# =================================================================
# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# © @G4rip (Telegram) - All Rights Reserved
# The features of this file are not available in the new version.
# You can contact @G4rip (Telegram) for this feature.
# =================================================================
# @G4rip - < https://t.me/G4rip >
# Telif hakkı (C) 2022
# © @G4rip (Telegram) - Tüm hakları saklıdır.
# Bu özellik yeni versiyonda kaldırılmıştır.
# Bu özellik için @G4rip (Telegram) ile iletişime geçebilirsiniz.
# =================================================================
#
#   @Client.on_message(filters.command("broadcast") & filters.reply)
#   async def broadcast_handler_open(_, m: Message):
#       if await dbsud.is_sudo_exist(m.from_user.id) is False:
#           return
#       await main_broadcast_handler(m, db)
#
#
#   @Client.on_message(
#       command("stats") & filters.user(SUDOS)
#   )
#   async def botstats(bot: Client, message: Message):
#
#       print(SUDOS)
#       chat_id = message.chat.id
#       lang = await get_str(chat_id)
#       LAN = lan(lang)
#       lol = await bot.send_message(
#           message.chat.id, LAN.WAIT_FOR_STATS.format(message.from_user.mention)
#       )
#       all_users = await dbsud.get_all_sudos()
#       groups = 0
#       pms = 0
#       async for user in all_users:
#           if str(user["id"]).startswith("-"):
#               groups += 1
#           else:
#               pms += 1
#       total, used, free = shutil.disk_usage(".")
#       total = humanbytes(total)
#       used = humanbytes(used)
#       free = humanbytes(free)
#       cpu_usage = psutil.cpu_percent()
#       ram_usage = psutil.virtual_memory().percent
#       disk_usage = psutil.disk_usage("/").percent
#       total_users = await db.total_users_count()
#       await lol.edit(
#           text=LAN.STATS.format(
#               BOT_USERNAME,
#               total_users,
#               groups,
#               pms,
#               total,
#               used,
#               disk_usage,
#               free,
#               cpu_usage,
#               ram_usage,
#               len(calisan),
#           ),
#           parse_mode=ParseMode.MARKDOWN,
#       )
#
#
#
#   @Client.on_message(filters.command("block"))
#   @sudo
#   async def ban(c: Client, m: Message):
#       chat_id = m.chat.id
#       lang = await get_str(chat_id)
#       LAN = lan(lang)
#       if m.reply_to_message:
#           user_id = m.reply_to_message.from_user.id
#           if len(m.command) <= 1:
#               ban_duration = 9999
#               ban_reason = LAN.BAN_REASON_1.format(BOT_USERNAME, GROUP_SUPPORT)
#           elif len(m.command) > 2:
#               ban_duration = 9999
#               ban_reason = " ".join(m.command[1:])
#       else:
#           if len(m.command) <= 1:
#               return await m.reply(LAN.NOT_USER)
#           elif len(m.command) == 2:
#               user_id = int(m.command[1])
#               ban_duration = 9999
#               ban_reason = LAN.BAN_REASON_1.format(BOT_USERNAME, GROUP_SUPPORT)
#           elif len(m.command) > 2:
#               user_id = int(m.command[1])
#               ban_duration = 9999
#               ban_reason = " ".join(m.command[2:])
#
#           if str(user_id).startswith("-"):
#               ban_log_text = LAN.BAN_REASON_2.format(
#                   m.from_user.mention, user_id, ban_duration, ban_reason
#               )
#               try:
#                   await c.send_message(
#                       user_id,
#                       LAN.BAN_REASON_3.format(
#                           ban_reason,
#                       ),
#                       reply_markup=InlineKeyboardMarkup(
#                           [
#                               [
#                                   InlineKeyboardButton(
#                                       LAN.SUPPORT_GROUP,
#                                       url=f"https://t.me/{GROUP_SUPPORT}",
#                                   )
#                               ]
#                           ]
#                       ),
#                   )
#                   await c.leave_chat(user_id)
#                   ban_log_text += LAN.BAN_REASON_4
#               except BaseException:
#                   traceback.print_exc()
#                   ban_log_text += LAN.BAN_REASON_5.format(traceback.format_exc())
#           else:
#               ban_log_text = LAN.BAN_REASON_6.format(
#                   m.from_user.mention, user_id, ban_duration, ban_reason
#               )
#               try:
#                   await c.send_message(
#                       user_id,
#                       LAN.BAN_REASON_7.format(ban_reason),
#                       reply_markup=InlineKeyboardMarkup(
#                           [
#                               [
#                                   InlineKeyboardButton(
#                                       LAN.SUPPORT_GROUP,
#                                       url=f"https://t.me/{GROUP_SUPPORT}",
#                                   )
#                               ]
#                           ]
#                       ),
#                   )
#                   await c.leave_chat(user_id)
#                   ban_log_text += LAN.BAN_REASON_8
#               except BaseException:
#                   traceback.print_exc()
#                   ban_log_text += LAN.BAN_REASON_9.format(traceback.format_exc())
#           await db.ban_user(user_id, ban_duration, ban_reason)
#           await c.send_message(LOG_CHANNEL[0], ban_log_text)
#           await m.reply_text(ban_log_text, quote=True)
#
#
#   @Client.on_message(filters.command("unblock"))
#   async def unban(c: Client, m: Message):
#       if await dbsud.is_sudo_exist(m.from_user.id) is False:
#           return
#       chat_id = m.chat.id
#       lang = await get_str(chat_id)
#       LAN = lan(lang)
#       if m.reply_to_message:
#           user_id = m.reply_to_message.from_user.id
#       else:
#           if len(m.command) <= 1:
#               return await m.reply(LAN.BAN_REASON_10.format(m.from_user.mention))
#           else:
#               user_id = int(m.command[1])
#       unban_log_text = LAN.BAN_REASON_11.format(m.from_user.mention, user_id)
#       if not str(user_id).startswith("-"):
#           try:
#               await c.send_message(user_id, LAN.BAN_REASON_12)
#               unban_log_text += LAN.BAN_REASON_8
#           except BaseException:
#               traceback.print_exc()
#               unban_log_text += LAN.BAN_REASON_9.format(traceback.format_exc())
#       await db.remove_ban(user_id)
#       await c.send_message(LOG_CHANNEL[0], unban_log_text)
#       await m.reply_text(unban_log_text, quote=True)
#
#
#   @Client.on_message(filters.command("blocklist"))
#   async def _banned_usrs(_, m: Message):
#       if await dbsud.is_sudo_exist(m.from_user.id) is False:
#           return
#       chat_id = m.chat.id
#       lang = await get_str(chat_id)
#       LAN = lan(lang)
#       all_banned_users = await db.get_all_banned_users()
#       banned_usr_count = 0
#       text = ""
#       async for banned_user in all_banned_users:
#           user_id = banned_user["id"]
#           ban_duration = banned_user["ban_status"]["ban_duration"]
#           banned_on = banned_user["ban_status"]["banned_on"]
#           ban_reason = banned_user["ban_status"]["ban_reason"]
#           banned_usr_count += 1
#           text += LAN.BAN_REASON_13.format(user_id, ban_duration, banned_on, ban_reason)
#       reply_text = LAN.BAN_REASON_14.format(banned_usr_count, text)
#       if len(reply_text) > 4096:
#           with open("banned-user-list.txt", "w") as f:
#               f.write(reply_text)
#           await m.reply_document("banned-user-list.txt", True)
#           os.remove("banned-user-list.txt")
#           return
#       await m.reply_text(reply_text, True)
#
