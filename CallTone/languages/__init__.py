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


from logging import getLogger

from Config import LANGUAGE

from ..database import get_lang
from . import CallTone_AZ, CallTone_EN, CallTone_RU, CallTone_TR

LOGS = getLogger(__name__)


async def get_str(chat_id: int):
    if await get_lang((chat_id)) == "TR":
        return "TR"
    elif await get_lang((chat_id)) == "EN":
        return "EN"
    elif await get_lang((chat_id)) == "AZ":
        return "AZ"
    elif await get_lang((chat_id)) == "RU":
        return "RU"
    else:
        return LANGUAGE


def lan(lang: str = None):
    if str(lang).upper() == "TR":
        LAN = CallTone_TR
    elif str(lang).upper() == "AZ":
        LAN = CallTone_AZ
    elif str(lang).upper() == "EN":
        LAN = CallTone_EN
    elif str(lang).upper() == "RU":
        LAN = CallTone_RU
    else:
        LAN = CallTone_TR
    return LAN
