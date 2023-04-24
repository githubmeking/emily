# -*- coding: utf-8 -*-

# (c) @aylak-github (Github) | https://t.me/ayIak | @BasicBots (Telegram)

#==============================================================================
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
#==============================================================================
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
#========================================================================


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
# @G4rip - < https://t.me/G4rip >
#
#   import os
#   
#   from PIL import Image
#   from pyrogram import Client
#   from pyrogram.enums import *
#   from pyrogram.types import Message
#   from Config import *
#   from ...languages import get_str, lan
#   from ..helpers import admin, command, extract_user, reload, block, cbblock
#   
#   
#   @Client.on_message(command(["stag"]) &~BANNED_CHATS &~BANNED_USERS)
#   @admin
#   @block
#   async def stag(client: Client, message: Message):
#       chat_id = message.chat.id
#       lang = await get_str(chat_id)
#       LAN = lan(lang)
#       await reload(client, message, message.from_user.id)
#       if message.chat.type == ChatType.PRIVATE:
#           return
#       try:
#           await message.delete()
#       except Exception:
#           pass
#       if not message.reply_to_message:
#           return await message.reply(LAN.STIC_NEED)
#       else:
#           if (
#               message.reply_to_message.sticker
#               or message.reply_to_message.document
#               or message.reply_to_message.photo
#           ):
#               if len(message.command) <= 1:
#                   return await message.reply(LAN.NOT_USER)
#               else:
#                   if message.reply_to_message.sticker:
#                       file_name = message.reply_to_message.sticker.file_name
#                       animation = message.reply_to_message.sticker.is_animated
#                       video = message.reply_to_message.sticker.is_video
#                       if file_name.endswith(".webp"):
#                           file = await message.reply_to_message.download(
#                               file_name="CallTone.webp"
#                           )
#                       elif animation:
#                           file = await message.reply_to_message.download(
#                               file_name="CallTone.tgs"
#                           )
#                       elif video:
#                           return await message.reply(LAN.VIDEO_STIC)
#                       user_id, _ = extract_user(message)
#                       try:
#                           user = await client.get_users(user_id)
#                       except Exception:
#                           return await message.reply(LAN.NO_USER)
#                       await client.send_document(
#                           chat_id=chat_id,
#                           document=file,
#                           # Idea Copyriht (C) 2022 @G4rip - < https://t.me/G4rip
#                           # > - All Rights Reserved
#                           caption=f"[ㅤㅤㅤㅤㅤㅤㅤㅤ](tg://user?id={user.id})",
#                       )
#                   elif (
#                       message.reply_to_message.document or message.reply_to_message.photo
#                   ):
#                       final = "calltone.webp"
#                       path_s = await message.reply_to_message.download()
#                       im = Image.open(path_s)
#                       im.save(final, "WEBP")
#                       user_id, _ = extract_user(message)
#                       try:
#                           user = await client.get_users(user_id)
#                       except Exception:
#                           return await message.reply(LAN.NO_USER)
#                       await client.send_document(
#                           chat_id=chat_id,
#                           document=final,
#                           # Idea Copyriht (C) 2022 @G4rip - < https://t.me/G4rip
#                           # > - All Rights Reserved
#                           caption=f"[ㅤㅤㅤㅤㅤㅤㅤ](tg://user?id={user.id})",
#                       )
#                       os.remove(final)
#                   else:
#                       return await message.reply(LAN.STIC_NEED)
#   
#           else:
#               return await message.reply(LAN.STIC_NEED)
#   