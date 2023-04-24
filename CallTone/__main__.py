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

from .core import *

# Programı Başlatma
async def start():
    await setSudoList()  # Sudo listesini ayarlar.
    await app.start()  # Botu başlatır.
    await setMaintenanceMode()  # Bakım modunu ayarlar.
    await setLogGroup()  # Log grubunu ayarlar.
    await setBotID()  # Bot ID'sini ayarlar.
    await setBannedUsers()  # Yasaklı kullanıcıları ayarlar.
    await setBannedChats()  # Yasaklı sohbetleri ayarlar.
    await editRestartMessage()  # Restart mesajını düzenler.
    await sendLogGroupStartMessage()  # Log grubuna başlama mesajı gönderir.
    await idle()  # Botu bekletir.
    await sendGroupStopMessage()  # Log grubuna kapatma mesajı gönderir.
    await app.stop()  # Botu durdurur.
    # exit(0) # Programı durdurur.

asyncio.run(start())  # Sistemi başlatır.
