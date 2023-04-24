import asyncio
import logging
import sys

from pyrogram import __version__, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pymongo import __version__ as pymongo_version

from Config import (
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    SUDOS,
    OWNER_ID,
    LOG_CHANNEL,
    black_list_chats,
    black_list_users,
    bakim
)

from pyromod import listen
from pythonansi import colors
from ..database import dbsud, keydb, USERS, CHATS, SUDO, BAKIM
from ..modules.helpers import FILE_CONTROL
from .client import app


color = colors()

# Restart mesajını düzenler.


async def setBotID():
    # global BOT_ID
    bot_id = (await app.get_me()).id
    BOT_ID.clear()
    BOT_ID.append(bot_id)

    color.print(f"Bot ID ayarlandı: {BOT_ID[0]}", color.green)


async def editRestartMessage():
    file = FILE_CONTROL("LAST_RESTART_MESSAGE")
    link = file.get()
    if (
        link
        and isinstance(link, str)
        and "|" in link
        and len(link.split("|")) == 2
        and link != ""
    ):
        try:
            # print(link, type(link))
            chat = int(link.split("|")[0])
            id = int(link.split("|")[1])
            await app.edit_message_text(
                chat, id, "**Bot başarıyla yeniden başlatıldı.**"
            )
        except Exception as e:
            print(str(e))

    file.del_()


# Log grubuna başlatma mesajı gönderir.

from requests import __version__ as requests_version


async def sendLogGroupStartMessage():
    print(SUDOS)
    uname = await app.get_me()
    try:
        users_count = len(await USERS().get_users())
        chats_count = len(await CHATS().get_chats())
        banned_users = len(await USERS().blocked_users())
        banned_chats = len(await CHATS().blacklisted_chats())
        sudos = len(await dbsud.get_all_sudos())
        text = f"""
**@{uname.username} Başarıyla başlatıldı!**

**🖥️ Sürümler:**
__Python Sürümü:__ `{sys.version.split()[0]}`
__MongoDB Sürümü:__ `{pymongo_version}`
__Pyrogram Sürümü:__ `{__version__}`
__Requests Sürümü:__ `{requests_version}`

**ℹ️ Bilgiler:**
__Bot ID:__ `{uname.id}`
__Bot Adı:__ `{uname.first_name}`
__Bot Kullanıcı Adı:__ @{uname.username}

**📚 Veriler:**
__Kullanıcılar:__ `{users_count}`
__Gruplar:__ `{chats_count}`
__Yasaklı Kullanıcılar:__ `{banned_users}` adet
__Yasaklı Sohbetler:__ `{banned_chats}` adet

__🕹️ Log Grubu:__ `{LOG_CHANNEL[0]}`

__🚨 Sudo Kullanıcıları:__ `{sudos}` adet

__👑By @BasicBots - @G4rip__
"""
        await app.send_message(
            LOG_CHANNEL[0],
            text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Destek Grubu", url="https://t.me/RepoHaneX"
                        ),
                    ],
                ],
            ),
        )
        color.print(f"Log Grubuna [{LOG_CHANNEL[0]}] başlatılma mesajı gönderildi.")
        a = f"""

    \033[32m Bot Started Successfully\033[0m

    \033[33m Bot Name: \033[0m {uname.first_name}\033[0m
    \033[33m Bot ID: \033[0m {uname.id}\033[0m
    \033[33m Bot Username: \033[0m @{uname.username}\033[0m

    \033[33m Pyrogram Version: \033[0m {__version__}\033[0m

    \033[33m Bot Version: \033[0m 3.0.0\033[0m
    """
        print(a)  # Bilgileri ekrana basar.
    except Exception:
        print(
            f"Log grubuna ( {LOG_CHANNEL[0]} ) erişim sağlanamadı. Lütfen botu gruba alıp tam yetki verin. Botun kullanıcı adı: @{uname.username}. İşlem durduruluyor..."
        )
        await app.stop()  # Stop the bot
        # sys.exit(143)  # Programı durdurur.


# Log grubuna kapatma mesajı gönderir.


async def sendGroupStopMessage():
    uname = await app.get_me()

    try:
        await app.send_message(
            LOG_CHANNEL[0],
            f"**@{uname.username}, Kapatıldı.**\n\n__By @BasicBots - @G4rip__",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Destek Grubu", url="https://t.me/RepoHaneX"
                        ),
                    ],
                ],
            ),
        )
        color.print(f"Log Grubuna [{LOG_CHANNEL[0]}] kapatılma mesajı gönderildi.")
    except Exception:
        print(
            f"Log grubuna ( {LOG_CHANNEL[0]} ) erişim sağlanamadı. Lütfen botu gruba alıp tam yetki verin. Botun kullanıcı adı: @{uname.username}. İşlem durduruluyor..."
        )
        await app.stop()  # Stop the bot
        # sys.exit(1)  # Programı durdurur.
    print(
        f"{color.red}@{uname.username} durduruldu!{color.reset}"
    )  # Kapatma mesajını ekrana basar.


# Bakim modunu ayarlar.

async def setMaintenanceMode():
    bakims = BAKIM()

    if await bakims.is_bakim():
        bakim.clear()
        bakim.append(True)
    else:
        bakim.clear()
        bakim.append(False)
    uname = await app.get_me()
    if await bakims.is_bakim():
        color.print("Bakım modu aktif edildi.", color.red)
        await app.send_message(
            LOG_CHANNEL[0],
            f"**@{uname.username} Bakım Moduna Alındı!**\n\n__By @BasicBot - @G4rip__",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Destek Grubu", url="https://t.me/RepoHaneX"
                        ),
                    ],
                ],
            ),
        )


# Sudo listesini düzenler.


async def setSudoList():
    # global SUDOS
    sudos = await dbsud.get_all_sudos()

    for sudo in sudos:
        SUDOS.append(int(sudo["id"]))
    color.print(
        f"Veritabanından {len(SUDOS)} tane sudo kullanıcı alındı ve kaydedildi.",
        color.yellow,
    )

    if OWNER_ID not in SUDOS:
        SUDOS.append(OWNER_ID)
        color.print("Bot sahibi sudo listesine kaydedildi.", color.green)
    color.print(f"Toplam {len(SUDOS)} tane sudo kullanıcı var.", color.yellow)


# Log grubunu ayarlar.


async def setLogGroup():
    # global LOG_CHANNEL[0]
    DB_LOG_CHANNEL = await keydb.get("LOG_CHANNEL")
    if DB_LOG_CHANNEL:
        LOG_CHANNEL.clear()
        LOG_CHANNEL.append(int(DB_LOG_CHANNEL))
        color.print(
            f"Log grubu veritabanından ayarlandı. [{LOG_CHANNEL[0]}]", color.yellow
        )
    else:
        #LOG_CHANNEL.clear()
        #LOG_CHANNEL.append(int(0))
        color.print("Log grubu Config'den ayarlandı.", color.red)


# Yasaklı Kullanıcılar listesini ayarlar.


async def setBannedUsers():
    # global black_list_users
    users = USERS()
    try:
        banned_users = await users.blocked_users()
    except Exception as e:
        color.print(f"Veritabanından yasaklı kullanıcı alınamadı. Hata: {e}", color.red)
        banned_users = None
        return
    if banned_users:
        for user in banned_users:
            black_list_users.append(user)
        color.print(
            f"Veritabanından {len(banned_users)} tane yasaklı kullanıcı alındı ve kaydedildi.",
            color.green,
        )
    else:
        color.print("Veritabanında yasaklı kullanıcı bulunmamakta", color.green)


# Yasaklı Sohbetler listesini ayarlar.


async def setBannedChats():
    # global black_list_chats
    chats = CHATS()
    try:
        banned_chats = await chats.blacklisted_chats()
    except Exception as e:
        color.print(f"Veritabanından yasaklı sohbet alınamadı. Hata: {e}", color.red)
        banned_chats = None
        return
    if banned_chats:
        for chat in banned_chats:
            black_list_users.append(chat)
        color.print(
            f"Veritabanından {len(banned_chats)} tane yasaklı sohbet alındı ve kaydedildi.",
            color.yellow,
        )
    else:
        color.print("Veritabanında yasaklı sohbet bulunmamakta.", color.yellow)
