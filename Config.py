# -*- coding: utf-8 -*-

# (c) @aylak-github (Github) | https://t.me/ayIak | @BasicBots (Telegram)
# ==============================================================================
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

import os
from os import getenv
from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

calisan = []

admins = {}

reasons = {}


ENV = os.environ.get("ENV", False)

if ENV:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_ID = int(getenv("BOT_ID"))
    BOT_TOKEN = getenv("BOT_TOKEN")
    BOT_USERNAME = getenv("BOT_USERNAME", "CallToneBot")
    BOT_NAME = getenv("BOT_NAME", "CallToneBot")
    OWNER_ID = int(getenv("OWNER_ID", 1769015061))
    DURATION = int(getenv("DURATION", 3))
    COUNT = int(getenv("COUNT", 6))
    COMMAND = getenv("COMMAND", "/")
    ADMIN = getenv("ADMIN")
    LANGUAGE = (getenv("LANGUAGE", "TR")).upper()
    LOG_CHANNEL = int(getenv("LOG_CHANNEL"))
    GROUP_SUPPORT = getenv("GROUP_SUPPORT")
    DATABASE_URL = getenv("DATABASE_URL")
    BROADCAST_AS_COPY = True if getenv("BROADCAST_AS_COPY") else False
    LOGGING = getenv("LOGGING", "Log")  # or GroupLog

else:
    API_ID = 11354711
    API_HASH = "cf17ce4aec110b1112b4996e4ac96f06"
    # "5118244333:AAEF80E3lszb2hVLkl4mZ1gVEkP9aPPKmaI" # @CallToneBot
    BOT_ID = []
    # "5073900336:AAG6RP_wjLBOGFagyKi8EElTfeC5zYc19I0"
    BOT_TOKEN = "5073900336:AAHMqmM75oFSKtaHEH4-fET281mT5oVvF_E"
    COMMAND = "/"
    BOT_USERNAME = "CallToneBot"
    BOT_NAME = "🎴 Call Tone Bot"
    OWNER_ID = 1769015061  # 5326318807
    DURATION = 3
    COUNT = 5
    ADMIN = "True"
    LANGUAGE = "TR"
    LOG_CHANNEL = [-1001757774317]
    GROUP_SUPPORT = "RepohaneX"
    DATABASE_URL = "mongodb+srv://lucis:lucis@cluster0.hpuze.mongodb.net/lucis?retryWrites=true&w=majority"
    # "mongodb+srv://aylak:aylak@cluster0.jyr2p.mongodb.net/Cluster0?retryWrites=true&w=majority"
    # "mongodb+srv://aylak:aylak@cluster0.ug9zn.mongodb.net/Cluster0?retryWrites=true&w=majority"
    # "mongodb+srv://lucis:lucis@cluster0.hpuze.mongodb.net/lucis?retryWrites=true&w=majority"

    SQL_DATABASE_URL = "postgres://ylggnwxd:4JZVBDenIwtHBR5S7szB133Pc54HYauo@tyke.db.elephantsql.com/ylggnwxd"
    BROADCAST_AS_COPY = False
    LOGGING = "Log"
    SUDOS = []

black_list_chats = []
black_list_users = []
# ================== #

bakim = [False]

BANNED_CHATS = filters.chat(black_list_chats)
BANNED_USERS = filters.user(black_list_users)
CHATS_CLEAN_MODE_SETTINGS = {}

# ================== #