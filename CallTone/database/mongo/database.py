# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# Tüm hakları saklıdır.
#
# Bu dosya, < https://github.com/aylak-github/CallTone > parçasıdır.
# Lütfen GNU Affero Genel Kamu Lisansını okuyun;
# < https://www.github.com/aylak-github/CallTone/blob/master/LICENSE/ >
# ================================================================

from datetime import datetime

import datetime as dt
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from Config import BOT_USERNAME, COUNT, DATABASE_URL, DURATION
from Config import *
from pyrogram import Client
from pyrogram.types import Chat, User, Message
from pyrogram.enums import ChatType

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
#   class Database:
#       def __init__(self, uri, database_name):
#           self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
#           self.db = self._client[database_name]
#           self.col = self.db.users
#
#       def new_user(self, id):
#           return dict(
#               id=id,
#               join_date=datetime.date.today().isoformat(),
#               ban_status=dict(
#                   is_banned=False,
#                   ban_duration=0,
#                   banned_on=datetime.date.max.isoformat(),
#                   ban_reason="",
#               ),
#           )
#
#       async def add_user(self, id):
#           user = self.new_user(id)
#           await self.col.insert_one(user)
#
#       async def is_user_exist(self, id):
#           user = await self.col.find_one({"id": int(id)})
#           return bool(user)
#
#       async def total_users_count(self):
#           count = await self.col.count_documents({})
#           return count
#
#       async def get_all_users(self):
#           return self.col.find({})
#
#       async def delete_user(self, user_id):
#           await self.col.delete_many({"id": int(user_id)})
#
#       async def remove_ban(self, id):
#           ban_status = dict(
#               is_banned=False,
#               ban_duration=0,
#               banned_on=datetime.date.max.isoformat(),
#               ban_reason="",
#           )
#           await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})
#
#       async def ban_user(self, user_id, ban_duration, ban_reason):
#           ban_status = dict(
#               is_banned=True,
#               ban_duration=ban_duration,
#               banned_on=datetime.date.today().isoformat(),
#               ban_reason=ban_reason,
#           )
#           await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})
#
#       async def get_ban_status(self, id):
#           default = dict(
#               is_banned=False,
#               ban_duration=0,
#               banned_on=datetime.date.max.isoformat(),
#               ban_reason="",
#           )
#           user = await self.col.find_one({"id": int(id)})
#           return user.get("ban_status", default)
#
#       async def get_all_banned_users(self):
#           return self.col.find({"ban_status.is_banned": True})
#
#
#   db = Database(DATABASE_URL, BOT_USERNAME)

chat_watcher_group = 10
MONGODB_CLI = MongoClient(DATABASE_URL)
db = MONGODB_CLI.basicbots

chatsdb = db.chats  # chatsdb is a collection of chats
usersdb = db.users  # usersdb is a collection of users
channeldb = db.channels
bloacked_usersdb = db.blocked_users  # blocked_usersdb is a collection of blocked users
blacklist_chatdb = db.blacklistChat  # blacklist_chatdb is a collection of blocked chats
bakim_modudb = db.bakim_modu  # bakim_modu is a collection of bakim_modu


##################### CHATS FUNCTIONS #####################


class CHATS:
    def __init__(self) -> None:
        pass

    async def is_chat(self, chat_id: int) -> bool:
        chat = await chatsdb.find_one({"chat_id": chat_id})
        if not chat:
            return False
        return True

    async def get_chats(self) -> list:
        chats = chatsdb.find({})  # "chat_id": {"$lt": 0}
        if not chats:
            return []  # empty list
        chats_list = []
        for chat in await chats.to_list(length=1000000000):
            chats_list.append(chat)
        return chats_list

    async def add_chat(self, bot: Client, chat: Chat, msg: Message):
        is_served = await self.is_chat(chat.id)
        if is_served:
            # print(f"{chat.id} is already served")
            return
        await chatsdb.insert_one({"chat_id": chat.id})
        text = " "
        if chat.type == ChatType.CHANNEL:
            a = (
                (f"\n__Kanal Kullanıcı Adı:__ @{chat.username}")
                if chat.username
                else ""
            )
            text += f"""**Yeni Kanal:**\n\n__**Kanal Adı:**__ {chat.title}\n__**Kanal ID:**__ {chat.id}{a}\n\n__**Eklenme Tarihi:**__ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n**Kanal Eklendi!\n\n#YENI_KANAL**"""
        elif chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            b = f"\n__Grup Kullanıcı Adı:__ @{chat.username}" if chat.username else ""
            text += f"**Yeni Grup:**\n\n__**Grup Adı:**__ {chat.title}\n__**Grup ID:**__ {chat.id}{b}\n__**Gruba Ekleyen Kullanıcı:**__ {msg.from_user.mention}\n__**Gruba Ekleyen Kullanıcı ID:**__ {msg.from_user.id}\n__**Eklenme Tarihi:**__ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n**Grup Eklendi!\n\n#YENI_GRUP**"
        else:

            c = (f"\n__Grup Kullanıcı Adı:__ @{chat.username}") if chat.username else ""
            text = f"__Bilinmeyen Sohbet({chat.type})__\n\n**Yeni Grup:**\n\n__**Grup Adı:**__ {chat.title}\n__**Grup ID:**__ {chat.id}{c}\n__**Gruba Ekleyen Kullanıcı:**__ {msg.from_user.mention}\n__**Gruba Ekleyen Kullanıcı ID:**__ {msg.from_user.id}\n__**Eklenme Tarihi:**__ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n**Grup Eklendi!\n\n#YENI_GRUP**"
        await bot.send_message(LOG_CHANNEL[0], text)

    async def remove_chat(self, chat_id: int):
        is_served = await self.is_chat(chat_id)
        if not is_served:
            return
        return await chatsdb.delete_one({"chat_id": chat_id})

    async def blacklisted_chats(self) -> list:
        chats = blacklist_chatdb.find({})
        chatss = []
        for user in await chats.to_list(length=1000000000):
            #print(user)
            chatss.append(user["chat_id"])
            
        return chatss
        # return [chat["chat_id"] for chat in await chats.to_list(length=1000000000)]

    async def blacklist_chat(self, chat_id: int) -> bool:
        if not await blacklist_chatdb.find_one({"chat_id": chat_id}):
            await blacklist_chatdb.insert_one({"chat_id": chat_id})
            return True
        return False

    async def white_list_chat(self, chat_id: int) -> bool:
        if await blacklist_chatdb.find_one({"chat_id": chat_id}):
            await blacklist_chatdb.delete_one({"chat_id": chat_id})
            return True
        return False


############### USERS FUNCTIONS ###############


class USERS:
    def __init__(self) -> None:
        pass

    async def is_user(self, user_id: int) -> bool:
        user = await usersdb.find_one({"user_id": user_id})
        if not user:
            return False
        return True

    async def get_users(self) -> list:
        users = usersdb.find({})  # "user_id": {"$lt": 0}
        if not users:
            return []  # empty list
        user_list = []
        for user in await users.to_list(length=1000000000):
            user_list.append(user)
        return user_list

    async def add_user(self, bot: Client, user: User):
        is_served = await self.is_user(user.id)
        if is_served:
            # print(f"{user.id} is already served")
            return
        await usersdb.insert_one({"user_id": user.id})
        text = f"**Yeni Kullanıcı:**\n\n__Kullanıcı:__ {user.mention}\n__Kullanıcı ID:__ {user.id}\n__Başlatma Tarihi:__ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n**Kullanıcı Eklendi!\n\n#YENI_KULLANICI**"
        await bot.send_message(LOG_CHANNEL[0], text)

    async def remove_user(self, user_id: int):
        user_is_served = await self.is_user(user_id)
        if not user_is_served:
            return
        return await usersdb.delete_one({"user_id": user_id})

    async def blocked_users(self) -> list:
        users = bloacked_usersdb.find({})
        userss = []
        for user in await users.to_list(length=1000000000):
            userss.append(user["user_id"])
            #print(userss)
        return userss  # [user["user_id"] for user in await users.to_list(length=1000000000)]

    async def block_user(self, user_id: int) -> bool:
        if not await bloacked_usersdb.find_one({"user_id": user_id}):
            await bloacked_usersdb.insert_one({"user_id": user_id})
            return True
        return False

    async def unblock_user(self, user_id: int) -> bool:
        if await bloacked_usersdb.find_one({"user_id": user_id}):
            await bloacked_usersdb.delete_one({"user_id": user_id})
            return True
        return False


##################### MAIN FUNCTIONS #####################
class BAKIM:
    def __init__(self) -> None:
        pass

    async def is_bakim(self) -> bool:
        bakim = await bakim_modudb.find_one({"bakim": True})
        # print(bakim)
        if not bakim:
            return False
        return True

    async def bakima_al(self):
        bakim = await self.is_bakim()
        if bakim:
            return
        await bakim_modudb.insert_one({"bakim": True})

    async def bakim_bitir(self):
        bakim = await self.is_bakim()
        if not bakim:
            return
        await bakim_modudb.delete_one({"bakim": True})


##################### SUDOS and BAKIM FUNCTIONS #####################
def bakim(mystic):
    async def wrapper(bot: Client, message: Message):
        b = await BAKIM().is_bakim()
        if b:
            return await message.reply_text(
                "**__Bakım aşamasındayım, şu anlık size hizmet veremem!__**"
            )
        return await mystic(bot, message)

    return wrapper





g4rip = MongoClient(DATABASE_URL)
mongo_handlers = g4rip.handlers

################### MONGODB COLLECTIONS ################
langdb = mongo_handlers.language  # langauge

delcmdmdb = mongo_handlers.admins  # delcmd

durationdb = mongo_handlers.duration  # duration

sudodb = mongo_handlers.sudos  # sudos

countdb = mongo_handlers.count  # count

################# VALUES #################


countdb = mongo_handlers.variable_value


class VARIABLE_VALUE:
    def __init__(self) -> None:
        pass

    async def get(self, key) -> int:
        cnt = await countdb.find_one({"variable": f"{key}"})
        if not cnt:
            return None
        return cnt["value"]

    async def set(self, key: str, value: (str | int)) -> None:
        await countdb.update_one(
            {f"variable": f"{key}"}, {"$set": {"value": value}}, upsert=True
        )

    async def del_(self, key: str) -> None:
        await countdb.delete_one({f"variable": f"{key}"})


keydb = VARIABLE_VALUE()
################ COUNTS ################


async def get_count(chat_id: int) -> int:
    cnt = await countdb.find_one({"chat_id": chat_id})
    if not cnt:
        # print(f"{chat_id} id grubun etiketleme sayısını belirlemesi gerekir. Etiketleme sayısı olmadığı için varsayılan sayı 5 olarak ayarlanmıştır.")
        return COUNT
    return cnt["count"]


async def set_count(chat_id: int, count: int) -> None:
    await countdb.update_one({"chat_id": chat_id}, {"$set": {"count": count}})


############### DURATIONS ################
async def get_duration(chat_id: int) -> int:
    dur = await durationdb.find_one({"chat_id": chat_id})
    if not dur:
        # print(f"{chat_id} adlı grubun etiketleme süresini belirlemesi gerekir. Etiketleme süresi olmadığı için varsayılan süre 5 saniye olarak ayarlanmıştır.")
        return DURATION
    return dur["duration"]


async def set_duration(chat_id: int, duration: int):
    await durationdb.update_one({"chat_id": chat_id}, {"$set": {"duration": duration}})


################### LANGUAGE ################
async def get_lang(chat_id: int) -> str:
    lang = await langdb.find_one({"chat_id": chat_id})
    if not lang:
        # print(f"{chat_id} adlı kullanıcının dilini belirlemesi gerekiyor. Dili olmadığı için varsayıln dil olarak TR olarak ayarlanıyor.")
        return "TR"
    return lang["lang"]


async def is_lang_exist(chat_id: int) -> bool:
    lang = await langdb.find_one({"chat_id": chat_id})
    return lang


async def lang_set(chat_id: int, lang: str):
    await langdb.update_one({"chat_id": chat_id}, {"$set": {"lang": lang}}, upsert=True)


################# CLEAN MODE ################
async def delcmd_is_on(chat_id: int) -> bool:
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int):
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})


################### SUDOS ###################
class SUDO:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.sudos

    def new_sudo(self, id):
        return dict(
            id=id,
            join_date=dt.date.today().isoformat(),
        )

    async def add_sudo(self, id):
        user = self.new_sudo(id)
        await self.col.insert_one(user)

    async def is_sudo_exist(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_sudos_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_sudos(self):
        users = self.col.find({})
        if not users:
            return []  # empty list
        user_list = []
        for user in await users.to_list(length=1000000000):
            user_list.append(user)
        return user_list

    async def delete_sudos(self, user_id):
        await self.col.delete_many({"id": int(user_id)})


dbsud = SUDO(DATABASE_URL, BOT_USERNAME)
