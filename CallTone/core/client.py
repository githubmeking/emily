
from pyrogram import Client, __version__

from Config import *


app = Client(
    name="CallTone",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="CallTone/modules"),
)


app.storage.SESSION_STRING_FORMAT = ">B?256sQ?"