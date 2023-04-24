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
import logging
import sys

from pyrogram import Client, __version__, idle
from tglogging import TelegramLogHandler

from Config import *

from pyromod import listen
from ..database import dbsud, keydb, USERS, CHATS
from .bot import (
    editRestartMessage,
    sendGroupStopMessage,
    setBannedUsers,
    setBannedChats,
    sendLogGroupStartMessage,
    setSudoList,
    setLogGroup,
    setBotID,
    setMaintenanceMode,
)
from .client import app

bot_version = "3.0.0"

# Log ayarları yapılır.

if LOGGING == "GroupLog":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        handlers=[
            TelegramLogHandler(
                token=BOT_TOKEN,
                log_chat_id=LOG_CHANNEL[0],
                update_interval=2,
                minimum_lines=1,  # Her Mesajda gönderilecek minimum satır sayısı
                pending_logs=200000,
            ),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger("CallTone")
    logger.info("Telegram'a canlı log başlatıldı.")
else:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    loger = logging.getLogger(__name__)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)
    print("CallTone - Terminal'e canlı log başlatıldı.")
