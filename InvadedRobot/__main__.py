import config
import media
import strings
import asyncio

from InvadedRobot import bot, inv
from InvadedRobot.helpers.status import status
from InvadedRobot.helpers.scandb import is_scan_user
from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums

@bot.on_message(filters.command("start"))
async def start(_, message):
   user_id = message.from_user.id
   if message.chat.type == enums.ChatType.PRIVATE:
     try:
         kk = await message.reply(text="`Analyzing The User`")
         await asyncio.sleep(2)
         mm = await kk.edit_text("`...`")
         await asyncio.sleep(1)
         ll = await mm.edit_text("`Processing...`")
         await asyncio.sleep(1)
         await ll.delete()
         is_rank = await status(user_id)
         is_scan = await is_scan_user(user_id)
         mention = message.from_user.mention
         await message.reply_photo(media.PM_PHOTO, caption=strings.PM_START_TEXT.format(mention, user_id,is_scan, is_rank))
     except Exception as e:
         await message.reply_photo(photo=(media.ERROR_IMG), caption=e)

   else:
     try:
         member_count = int(await bot.get_chat_members_count(message.chat.id))
         msg_count = int(await inv.search_messages_count(message.chat.id))
         kk = await message.reply(text="`Analyzing The User`")
         await asyncio.sleep(2)
         mm = await kk.edit_text("`...`")
         await asyncio.sleep(1)
         ll = await mm.edit_text("`Processing...`")
         await asyncio.sleep(1)
         await ll.delete()
         chat_title = message.chat.title
         chat_id = message.chat.id
         await message.reply_photo(media.PM_PHOTO, caption=strings.GROUP_START_TEXT.format(chat_title,chat_id, member_count,msg_count))
     except Exception as e:
         await message.reply_photo(photo=(media.ERROR_IMG), caption=e)

if __name__ == "__main__":
     bot.run()
     with bot:
        bot.send_photo(chat_id=config.LOG_GROUP_ID,photo=(media.INVADED_IMG),caption="<b>I'm Awake Already!</b>",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣!",url=f"{config.GROUP_URL}")]]))
