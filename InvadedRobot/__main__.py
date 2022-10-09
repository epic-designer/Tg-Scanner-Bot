import config
import media
from strings import *
import asyncio

from InvadedRobot import bot, inv
from InvadedRobot.helpers.status import status
from InvadedRobot.helpers.scandb import is_scan_user
from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums

BUTTON = InlineKeyboardMarkup([[
InlineKeyboardButton("🔔",url=config.UPDATE_CHANNEL_URL),
InlineKeyboardButton("🔊",url=config.LOG_CHANNEL_URL),
InlineKeyboardButton("📊",url=config.SYSTEM_CHANNEL_URL),],[
InlineKeyboardButton("🆘",callback_data="help"),]])

@bot.on_message(filters.command("start"))
async def start(_, message):
   user_id = message.from_user.id
   if message.chat.type == enums.ChatType.PRIVATE:
     try:
         kk = await message.reply(text="`Analyzing The User`")
         await asyncio.sleep(2)
         await kk.edit(ANI0)
         await asyncio.sleep(1)
         await kk.edit(ANI1)
         await asyncio.sleep(1)
         await kk.edit(ANI2)
         await asyncio.sleep(1)
         await kk.edit(ANI3)
         await asyncio.sleep(1)
         await kk.edit(ANI4)
         await asyncio.sleep(1)
         await kk.edit(ANI5)
         await asyncio.sleep(1)
         await kk.edit(ANI6)
         await asyncio.sleep(1)
         await kk.delete() 
         is_rank = await status(user_id)
         is_scan = await is_scan_user(user_id)
         mention = message.from_user.mention
         await message.reply_photo(media.PM_PHOTO, caption=PM_START_TEXT.format(mention, user_id,is_scan, is_rank),reply_markup=BUTTON)
     except Exception as e:
         await message.reply_photo(photo=(media.ERROR_IMG), caption=f"`{e}`")

   else:
     try:
         member_count = int(await bot.get_chat_members_count(message.chat.id))
         msg_count = int(await inv.search_messages_count(message.chat.id))
         chat_title = message.chat.title
         chat_id = message.chat.id
         await message.reply_photo(media.PM_PHOTO, caption=GROUP_START_TEXT.format(chat_title,chat_id, member_count,msg_count),reply_markup=BUTTON)
     except Exception as e:
         await message.reply_photo(photo=(media.ERROR_IMG), caption=f"`{e}`")

if __name__ == "__main__":
     bot.run()
     with bot:
        bot.send_photo(chat_id=config.LOG_GROUP_ID,photo=(media.INVADED_IMG),caption="<b>I'm Awake Already!</b>",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣!",url=f"{config.GROUP_URL}")]]))
