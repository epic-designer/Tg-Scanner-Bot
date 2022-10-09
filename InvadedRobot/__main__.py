import config
import media
import asyncio
from InvadedRobot import bot
from InvadedRobot.helpers.status import status
from InvadedRobot.helpers.scandb import is_scan_user
from pyrogram import filters
from pyrogram.types import *
from pyrogram import enums

PM_PHOTO = "https://telegra.ph/file/e9a7b101e8fcc7e6b7381.jpg"


PM_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`
**Invaded Analysis Report :-**
 ➛ **User:** {}
 ➛ **ID:** `{}`
 ➛ **Is Restricted:** `{}`
 ➛ **Status:** `{}`
 ➛ **Crime Coefficient:** `Under - 100`
"""

@bot.on_message(filters.command("start"))
async def start(_, message):
   user_id = message.from_user.id
   if message.chat.type == enums.ChatType.PRIVATE:
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
        await message.reply_photo(PM_PHOTO, caption=PM_START_TEXT.format(mention, user_id,is_scan, is_rank))


if __name__ == "__main__":
     bot.run()
     with bot:
        bot.send_photo(chat_id=config.LOG_GROUP_ID,photo=(media.INVADED_IMG),caption="<b>I'm Awake Already!</b>",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣!",url=f"{config.GROUP_URL}")]]))
