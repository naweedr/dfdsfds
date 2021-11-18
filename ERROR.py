from pyrogram import Client
from pyrogram import filters
from pyrogram import idle
from pyrogram import errors

from pyrogram.types import InlineKeyboardButton as button
from pyrogram.types import InlineKeyboardMarkup as markup
from pyrogram.types import ForceReply as reply

api_id, api_hash = 164723, "dabd3508016970f6c78c43ab208415da"
with Client("session_me",api_id,api_hash) as cli:
    cli.send_message("me","Developer : @Add_GptoGp")

    
