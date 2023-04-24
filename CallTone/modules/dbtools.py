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
from pyrogram import Client, filters
from pyrogram.types import Message
from Config import BROADCAST_AS_COPY, GROUP_SUPPORT, LOG_CHANNEL, SUDOS as SUDO_USERS
from ..database import CHATS, USERS
from Config import *
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client
from pyrogram.enums.chat_type import ChatType
from pyromod import listen
import asyncio
from pymongo import __version__ as mongo_version
from pyrogram import __version__ as pyrogram_version
from pyrogram.errors import ButtonUrlInvalid, FloodWait
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
import platform, psutil
from .helpers import command, sudo, cbsudo, block, cbblock

chat_watcher_group = 10

bot_version = "3.0.0 Beta 1.3.5"

pin = False

@Client.on_message(command("stats"))
@sudo
@block
async def stats(bot: Client, message: Message):
    chats_ = CHATS()
    users_ = USERS()

    platform_ = f"{platform.system()} {platform.release()}"
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    psyhical_cores = psutil.cpu_count(logical=False)
    total_cores = psutil.cpu_count(logical=True)
    cpu_usage = str(psutil.cpu_percent()) + "%"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHz"
    except:
        cpu_freq = "Alınamadı"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total).split(".")[0]
    used = hdd.used / (1024.0**3)
    used = str(used).split(".")[0]
    free = hdd.free / (1024.0**3)
    free = str(free).split(".")[0]

    schats = await chats_.get_chats()
    susers = await users_.get_users()

    chats = [int(chat["chat_id"]) for chat in schats]
    users = [int(user["user_id"]) for user in susers]

    pms = len(users)
    chat_ = len(chats)

    text = f"""**🤖 Botun İstatistikleri**\n
**🖥️ Sunucu Bilgileri**
    ** Platform:** `{platform_}`
    ** RAM:** `{ram}`
    ** CPU:** `{psyhical_cores} Çekirdek ({total_cores} Toplam)`
    ** CPU Kullanımı:** `{cpu_usage}`
    ** CPU Frekansı:** `{cpu_freq}`
    ** HDD:** `{total}` GB (`{used} GB Kullanıldı, {free} GB Boş`)

**📊 Kayıtlı Veriler**
    **👥 Grup Sayısı:** `{chat_}`
    **👤 Kullanıcı Sayısı:** `{pms}`
    **👾 Toplam Sohbetler:** `{chat_ + pms}`
    
** 🔥 Versiyonlar**
    **🤖 Bot Versiyonu:** `{bot_version}`
    **📝 MongoDB Versiyonu:** `{mongo_version}`
    **📝 Pyrogram Versiyonu:** `{pyrogram_version}`
    **📝 Python Versiyonu:** `{platform.python_version()}`

"""

    await message.reply_text(text)


###################### ADD TO DATABASE ##############################
@Client.on_message(group=chat_watcher_group)
@block
async def chat_watcher_func(bot: Client, message: Message):
    chats = CHATS()
    users = USERS()
    if message.from_user.id is None:
        return # await message.reply_text("Anonim kullanıcılar desteklenmiyor!")

    if message.chat.type == ChatType.PRIVATE:
        user = message.from_user
        await users.add_user(bot, user=user)
    else:
        chat = message.chat
        blacklisted_chats_list = await chats.blacklisted_chats()
        if chat.id in blacklisted_chats_list:
            return await bot.leave_chat(chat.id)
        await chats.add_chat(bot, message.chat, message)


@Client.on_message(filters.command(["send"]))
@sudo
@block
async def send(client: Client, message: Message):
    user = True
    chat = True
    pin = False
    if len(message.text.split()) < 3:
        await message.reply_text("**Kullanım**:\n/broadcast [buton adı:buton linki]")
        return
    if not message.reply_to_message:
        return await message.reply_text("**Lütfn bir mesajı yanıtlayın!**")

    link = message.text.split()[len(message.text.split()) - 1]
    button = message.text.split()[len(message.text.split()) - 2]

    msg = message.reply_to_message
    if "-user" in message.text:
        user = False
    if "-chat" in message.text:
        chat = False
    if "-pin" in message.text:
        pin = True
    try:
        a = await client.send_message(
            LOG_CHANNEL[0],
            button,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=button,
                            url=link,
                        ),
                    ],
                ],
            ),
        )
    except ButtonUrlInvalid:
        await message.reply("Link Hatalı! Lütfen linki kontrol edip tekrar deneyin.")
        await a.delete()
        return
    except Exception as e:
        await message.reply(f"Hata: {e}")
        await a.delete()
        return
    await a.delete()

    chats_ = CHATS()
    users_ = USERS()
    pinned = 0
    sleep_time = 0.1
    send_chats = 0
    send_pms = 0
    schats = await chats_.get_chats()
    susers = await users_.get_users()
    usersss = [int(user["user_id"]) for user in susers]
    chats = [int(chat["chat_id"]) for chat in schats]

    m = await message.reply(
        f"Yayın devam ediyor, Tahmini {(len(chats) + len(usersss) ) * sleep_time} saniye sürecek. Bittiğinde bir mesaj gönderilecek."
    )
    if chat is True:
        for i in chats:
            try:
                a = await msg.copy(
                    i,
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text=button, url=link)]]
                    ),
                )
                await asyncio.sleep(sleep_time)
                if pin is True:
                    try:
                        await a.pin(disable_notification=False)
                        pinned += 1
                    except:
                        pass
                send_chats += 1
            except FloodWait as e:
                await asyncio.sleep(int(e.x))
            except Exception:
                pass
        await client.send_message(
            message.chat.id,
            f"✈️ **{send_chats} tane gruba gönderildi.\n {pinned} tane grupta sabitlendi!**",
        )
    if user is True:
        for i in usersss:
            try:
                await msg.copy(
                    i,
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text=button, url=link)]]
                    ),
                )
                await asyncio.sleep(sleep_time)
                send_pms += 1
            except FloodWait as e:
                await asyncio.sleep(int(e.x))
            except Exception:
                pass
        await client.send_message(
            message.chat.id, f"✈️ **{send_pms} tane kullanıcıya gönderildi**"
        )
    await m.delete()





@Client.on_message(filters.command(["yayin", "broadcast"]))
@sudo
async def broadcast_message(bot: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("**Kullanım**:\n/broadcast [yanıtlanan mesaj]")

    msg = message.reply_to_message
    fmsg = await msg.forward(message.chat.id)
    text = f"""Göndereceğiniz gönderi yukarıda verilmiştir. Aşağıdaki butonlardan seçim yapınız.
    
    
İletilsin mi?: Evet (Eğer iletilmezse mesajın kopyası gönderilir)
Gruplara gönderilsin mi?: Evet 
Kullanıcılara gönderilsin mi?: Evet
    """

    await bot.send_message(
        message.chat.id,
        text=text,
        reply_to_message_id=fmsg.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Gruplar ✅", callback_data="broadcast_groups Evet"
                    ),
                    InlineKeyboardButton(
                        "Kullanıcılar ✅", callback_data="broadcast_users Evet"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "İletilsin mi? ✅", callback_data="forward Evet"
                    ),
                    InlineKeyboardButton(
                        "Sabitlensin mi? ❌", callback_data="pin Hayır"
                    ),
                ],
                [
                    InlineKeyboardButton("Gönder 📤", callback_data="send_broadcast"),
                    InlineKeyboardButton("İptal ⛔️", callback_data="stop_broadcast"),
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex(r"broadcast_groups"))
@cbsudo
async def broadcast_groups(bot: Client, query: CallbackQuery):
    text = query.message.text
    mevcut_gruplar = query.data.split(" ")[1]
    mevcut_iletilme = (text.split("İletilsin mi?: ")[1]).split(" ")[0]
    mevcut_kullanicilar = (text.split("Kullanıcılara gönderilsin mi?: ")[1]).split(
        "\n"
    )[0]
    groups_button_icon = "❌" if mevcut_gruplar == "Evet" else "✅"
    iletilme_button_icon = "✅" if mevcut_iletilme == "Evet" else "❌"
    kullnicilar_button_icon = "✅" if mevcut_kullanicilar == "Evet" else "❌"
    yeni_gruplar = "Hayır" if mevcut_gruplar == "Evet" else "Evet"
    yeni_iletilme = "Evet" if mevcut_iletilme == "Evet" else "Hayır"
    yeni_kullanicilar = "Evet" if mevcut_kullanicilar == "Evet" else "Hayır"
    yeni_yazi = "Gruplara gönderilsin mi?: " + yeni_gruplar
    replaced_text = (
        "Gruplara gönderilsin mi?: Evet"
        if mevcut_gruplar == "Evet"
        else "Gruplara gönderilsin mi?: Hayır"
    )
    sabitlensinmi = "Sabitlensin mi? ✅" if pin is True else "Sabitlensin mi? ❌"
    print(replaced_text)
    new_text = text.replace(replaced_text, yeni_yazi)
    await query.edit_message_text(
        new_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Gruplar " + groups_button_icon,
                        callback_data="broadcast_groups " + yeni_gruplar,
                    ),
                    InlineKeyboardButton(
                        "Kullanıcılar " + kullnicilar_button_icon,
                        callback_data="broadcast_users " + yeni_kullanicilar,
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "İletilsin mi? " + iletilme_button_icon,
                        callback_data="forward " + yeni_iletilme,
                    ),
                    InlineKeyboardButton(sabitlensinmi, callback_data="pin"),
                ],
                [
                    InlineKeyboardButton("Gönder 📤", callback_data="send_broadcast"),
                    InlineKeyboardButton("İptal ⛔️", callback_data="stop_broadcast"),
                ],
            ]
        ),
    )


@Client.on_callback_query(
    filters.regex("stop_broadcast")
    & filters.user(SUDO_USERS)
    & ~BANNED_CHATS
    & ~BANNED_USERS
)
@cbsudo
async def stop_broadcast(bot: Client, query: CallbackQuery):
    deleted_msg = query.message.reply_to_message
    await deleted_msg.delete()
    await query.message.edit("Gönderi iptal edildi.")
    await query.answer("Gönderi silindi.", show_alert=True)


@Client.on_callback_query(filters.regex(r"broadcast_users"))
@cbsudo
async def broadcast_users(bot: Client, query: CallbackQuery):
    text = query.message.text  # mesajın textini al
    mevcut_kullanicilar = query.data.split(" ")[1]  # mevcut kullanıcıların bilgisini al
    mevcut_iletilme = (text.split("İletilsin mi?: ")[1]).split(" ")[0]
    mevcut_gruplar = (text.split("Gruplara gönderilsin mi?: ")[1]).split("\n")[0]
    print(mevcut_iletilme)
    groups_button_icon = "✅" if mevcut_gruplar.strip() == "Evet" else "❌"
    iletilme_button_icon = "✅" if mevcut_iletilme.strip() == "Evet" else "❌"
    sabitlensinmi = "Sabitlensin mi? ✅" if pin is True else "Sabitlensin mi? ❌"
    if mevcut_kullanicilar == "Evet":
        yeni_kullanicilar = "Hayır"
        kullanici_buton_icon = "❌"
        new_users_text = "Kullanıcılara gönderilsin mi?: " + yeni_kullanicilar
        new_text = text.replace("Kullanıcılara gönderilsin mi?: Evet", new_users_text)
    elif mevcut_kullanicilar == "Hayır":
        yeni_kullanicilar = "Evet"
        kullanici_buton_icon = "✅"
        new_users_text = "Kullanıcılara gönderilsin mi?: " + yeni_kullanicilar
        new_text = text.replace("Kullanıcılara gönderilsin mi?: Hayır", new_users_text)
    await query.edit_message_text(
        new_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Gruplar " + groups_button_icon,
                        callback_data="broadcast_groups " + yeni_kullanicilar,
                    ),
                    InlineKeyboardButton(
                        "Kullanıcılar " + kullanici_buton_icon,
                        callback_data="broadcast_users " + yeni_kullanicilar,
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "İletilsin mi? " + iletilme_button_icon,
                        callback_data="forward " + yeni_kullanicilar,
                    ),
                    InlineKeyboardButton(sabitlensinmi, callback_data="pin"),
                ],
                [
                    InlineKeyboardButton("Gönder 📤", callback_data="send_broadcast"),
                    InlineKeyboardButton("İptal ⛔️", callback_data="stop_broadcast"),
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex(r"forward"))
@cbsudo
async def forward_braoadcast(bot: Client, query: CallbackQuery):
    text = query.message.text
    mevcut_iletilme = query.data.split(" ")[1]  # iletilme durumunu al
    mevcut_gruplar = (text.split("Gruplara gönderilsin mi?: ")[1]).split("\n")[0]
    mevcut_kullanicilar = (text.split("Kullanıcılara gönderilsin mi?: ")[1]).split(
        "\n"
    )[0]
    groups_button_icon = "✅" if mevcut_gruplar.strip() == "Evet" else "❌"
    users_button_icon = "✅" if mevcut_kullanicilar.strip() == "Evet" else "❌"
    sabitlensinmi = "Sabitlensin mi? ✅" if pin is True else "Sabitlensin mi? ❌"
    if mevcut_iletilme == "Evet":
        yeni_iletilme = "Hayır"
        new_forward_text = "İletilsin mi?: Hayır"
        forward_button_icon = "❌"
        new_text = text.replace("İletilsin mi?: Evet", new_forward_text)
    elif mevcut_iletilme == "Hayır":
        yeni_iletilme = "Evet"
        new_forward_text = "İletilsin mi?: Evet"
        forward_button_icon = "✅"
        new_text = text.replace("İletilsin mi?: Hayır", new_forward_text)
    await query.edit_message_text(
        new_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"Gruplar {groups_button_icon}",
                        callback_data=f"broadcast_groups {mevcut_gruplar}",
                    ),
                    InlineKeyboardButton(
                        f"Kullanıcılar {users_button_icon}",
                        callback_data=f"broadcast_users {mevcut_kullanicilar}",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        f"İletilsin mi? {forward_button_icon}",
                        callback_data=f"forward {yeni_iletilme}",
                    ),
                    InlineKeyboardButton(sabitlensinmi, callback_data="pin"),
                ],
                [
                    InlineKeyboardButton("Gönder 📤", callback_data="send_broadcast"),
                    InlineKeyboardButton("İptal ⛔️", callback_data="stop_broadcast"),
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex(r"pin"))
@cbsudo
async def pin_broadcast(bot: Client, query: CallbackQuery):
    global pin
    text = query.message.text
    #mevcut_iletilme = query.data.split(" ")[1]  # iletilme durumunu al
    mevcut_gruplar = (text.split("Gruplara gönderilsin mi?: ")[1]).split("\n")[0]
    mevcut_kullanicilar = (text.split("Kullanıcılara gönderilsin mi?: ")[1]).split(
        "\n"
    )[0]
    groups_button_icon = "✅" if mevcut_gruplar.strip() == "Evet" else "❌"
    users_button_icon = "✅" if mevcut_kullanicilar.strip() == "Evet" else "❌"
    sabitlensinmi = "Sabitlensin mi? ✅" if pin is True else "Sabitlensin mi? ❌"
    
    
    mevcut_iletilme = (text.split("İletilsin mi?: ")[1]).split(" ")[0]
    iletilme_button_icon = "✅" if mevcut_iletilme.strip() == "Evet" else "❌"
    if pin is True:
        pin = False
        sabitlensinmi = "Sabitlensin mi? ❌"
    elif pin is False:
        pin = True
        sabitlensinmi = "Sabitlensin mi? ✅"


    await query.edit_message_text(
       text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"Gruplar {groups_button_icon}",
                        callback_data=f"broadcast_groups {mevcut_gruplar}",
                    ),
                    InlineKeyboardButton(
                        f"Kullanıcılar {users_button_icon}",
                        callback_data=f"broadcast_users {mevcut_kullanicilar}",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        f"İletilsin mi? {iletilme_button_icon}",
                        callback_data=f"forward {mevcut_iletilme}",
                    ),
                    InlineKeyboardButton(sabitlensinmi, callback_data="pin"),
                ],
                [
                    InlineKeyboardButton("Gönder 📤", callback_data="send_broadcast"),
                    InlineKeyboardButton("İptal ⛔️", callback_data="stop_broadcast"),
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex(r"send_broadcast"))
@cbsudo
async def send_broadcast(bot: Client, query: CallbackQuery):
    query_text = query.message.text

    broadcasted_message = query.message.reply_to_message
    groupss = (query_text.split("Gruplara gönderilsin mi?: ")[1]).split(" ")[0]
    userss = (query_text.split("Kullanıcılara gönderilsin mi?: ")[1]).split(" ")[0]
    forwarded = (query_text.split("İletilsin mi?: ")[1]).split(" ")[0]


    if forwarded == "Evet":
        forward = True
    elif forwarded == "Hayır":
        forward = False

    if groupss == "Evet":
        groups = True
    elif groupss == "Hayır":
        groups = False

    if userss == "Evet":
        users = True
    elif userss == "Hayır":
        users = False

    if groups is False and users is False:
        await query.message.edit(
            "Gönderinin gönderileceği kimse seçilmedi.",
        )
        return
    chats_, users_ = CHATS(), USERS()
    sleep_time = 0.1
    send_chats = 0
    send_pms = 0
    schats = await chats_.get_chats()
    susers = await users_.get_users()
    usersss = [int(user["user_id"]) for user in susers]
    chats = [int(chat["chat_id"]) for chat in schats]

    m = await query.message.edit(
        f"Yayın devam ediyor, Tahmini {(len(chats) + len(usersss) ) * sleep_time} saniye sürecek. Bittiğinde bir mesaj gönderilecek."
    )
    if groups is True:
        for i in chats:
            try:
                if forward is True:
                    a = await broadcasted_message.forward(i)
                    try:
                        if pin is True:
                            await a.pin()
                    except Exception:
                        pass
                else:
                    a = await broadcasted_message.copy(i)
                    try:
                        if pin is True:
                            await a.pin()
                    except Exception:
                        pass
                await asyncio.sleep(sleep_time)
                send_chats += 1
            except FloodWait as e:
                await asyncio.sleep(int(e.x))
            except Exception:
                pass
        await bot.send_message(
            query.message.chat.id, f"✈️ **{send_chats} tane gruba gönderildi**"
        )
    if users is True:
        for i in usersss:
            try:
                if forward is True:
                    await broadcasted_message.forward(i)
                else:
                    await broadcasted_message.copy(i)
                await asyncio.sleep(sleep_time)
                send_pms += 1
            except FloodWait as e:
                await asyncio.sleep(int(e.x))
            except Exception:
                pass
        await bot.send_message(
            query.message.chat.id, f"✈️ **{send_pms} tane kullanıcıya gönderildi**"
        )


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
#   async def handle_user_status(bot: Client, cmd: Message):
#       chat_id = cmd.chat.id
#       if not await db.is_user_exist(chat_id):
#           if cmd.chat.type == ChatType.PRIVATE:
#               await db.add_user(chat_id)
#               await bot.send_message(
#                   LOG_CHANNEL[0],
#                   f"```📣 Yeni Bildirim``` \n\n#YENI_KULLANICI **botu başlattı!** \n\n🏷 isim: `{cmd.from_user.first_name}` \n📮 kullanıcı id: `{cmd.from_user.id}` \n🧝🏻‍♂️ profil linki: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})",
#               )
#           else:
#               await db.add_user(chat_id)
#               chat = await bot.get_chat(chat_id)
#               await bot.send_message(
#                   LOG_CHANNEL[0],
#                   f"```📣 Yeni Bildirim``` \n\n#YENI_GRUP **botu başlattı!** \n\n🏷 Gruba Alan İsim: `{cmd.from_user.first_name}` \n📮 Gruba Alan kullanıcı id: `{cmd.from_user.id}` \n🧝🏻‍♂️ profil linki: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n Grubun Adı: {chat.title}\n Grubun ID: {cmd.chat.id}\n Grubun Mesaj Linki( sadece açık gruplar): [Buraya Tıkla](https://t.me/c/{cmd.chat.id}/1)",
#               )
#
#       ban_status = await db.get_ban_status(chat_id)
#       if ban_status["is_banned"]:
#           if int(
#               (
#                   datetime.date.today()
#                   - datetime.date.fromisoformat(ban_status["banned_on"])
#               ).days
#           ) > int(ban_status["ban_duration"]):
#               await db.remove_ban(chat_id)
#           else:
#               if cmd.chat.type == ChatType.PRIVATE:
#                   await bot.send_message(
#                       cmd.chat.id,
#                       f"Üzgünüm, yasaklandınız! Çözüm için @{GROUP_SUPPORT}'a bekleriz.",
#                   )
#               else:
#                   await bot.send_message(
#                       cmd.chat.id,
#                       f"Üzgünüm, grubunuz karalisteye alındı! Burada daha fazla kalamam. Destek için @{GROUP_SUPPORT}'e gelin.",
#                   )
#                   await bot.leave_chat(cmd.chat.id)
#
#               return
#       await cmd.continue_propagation()


#   broadcast_ids = {}
#
#
#   async def send_msg(user_id, message):
#       try:
#           if BROADCAST_AS_COPY is False:
#               await message.forward(chat_id=user_id)
#           elif BROADCAST_AS_COPY is True:
#               await message.copy(chat_id=user_id)
#           return 200, None
#       except FloodWait as e:
#           await asyncio.sleep(int(e.x))
#           return send_msg(user_id, message)
#       except InputUserDeactivated:
#           return 400, f"{user_id} : aktif değil\n"
#       except UserIsBlocked:
#           return 400, f"{user_id} : botu engellemiş\n"
#       except PeerIdInvalid:
#           return 400, f"{user_id} : kullanıcı kimliği yanlış\n"
#       except Exception:
#           return 500, f"{user_id} : {traceback.format_exc()}\n"
#
#
#   async def main_broadcast_handler(m, db):
#       all_users = await db.get_all_users()
#       broadcast_msg = m.reply_to_message
#       while True:
#           broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
#           if not broadcast_ids.get(broadcast_id):
#               break
#       out = await m.reply_text(
#           text="```📤 BroadCast başlatıldı! Bittiği zaman mesaj alacaksınız!"
#       )
#
#       start_time = time.time()
#       total_users = await db.total_users_count()
#       done = 0
#       failed = 0
#       success = 0
#       broadcast_ids[broadcast_id] = dict(
#           total=total_users, current=done, failed=failed, success=success
#       )
#       async with aiofiles.open("broadcast-logs.txt", "w") as broadcast_log_file:
#           async for user in all_users:
#               sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
#               if msg is not None:
#                   await broadcast_log_file.write(msg)
#               if sts == 200:
#                   success += 1
#               else:
#                   failed += 1
#               if sts == 400:
#                   await db.delete_user(user["id"])
#               done += 1
#               if broadcast_ids.get(broadcast_id) is None:
#                   break
#               else:
#                   broadcast_ids[broadcast_id].update(
#                       dict(current=done, failed=failed, success=success)
#                   )
#       if broadcast_ids.get(broadcast_id):
#           broadcast_ids.pop(broadcast_id)
#       completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
#       await asyncio.sleep(3)
#       await out.delete()
#       if failed == 0:
#           await m.reply_text(
#               text=f"✅ ```Broadcast başarıyla tamamlandı``` \n\n**Tamamlanan:** `{completed_in}` \n\n**Toplam:** `{total_users}` \n\n**Total done:** `{done}` \n\n**Toplam tamamlanan:** `{success}` \n\n**Toplam hata:** `{failed}`",
#               quote=True,
#           )
#       else:
#           await m.reply_document(
#               document="broadcast-logs.txt",
#               caption=f"✅ ```Broadcast başarıyla tamamlandı``` \n\n**Tamamlanan:** `{completed_in}` \n\n**Toplam:** `{total_users}` \n\n**Total done:** `{done}` \n\n**Toplam tamamlanan:** `{success}` \n\n**Toplam hata:** `{failed}`",
#               quote=True,
#           )
#       os.remove("broadcast-logs.txt")
#
#
#   delcmdmdb = mongo_handlers.admins
#
#
#   async def delcmd_is_on(chat_id: int) -> bool:
#       chat = await delcmdmdb.find_one({"chat_id": chat_id})
#       return not chat
#
#
#   async def delcmd_on(chat_id: int):
#       already_del = await delcmd_is_on(chat_id)
#       if already_del:
#           return
#       return await delcmdmdb.delete_one({"chat_id": chat_id})
#
#
#   async def delcmd_off(chat_id: int):
#       already_del = await delcmd_is_on(chat_id)
#       if not already_del:
#           return
#       return await delcmdmdb.insert_one({"chat_id": chat_id})
