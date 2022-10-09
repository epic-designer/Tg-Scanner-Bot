import config
import strings

from pyrogram import filters
from pyrogram.types import *
from InvadedRobot import bot
from InvadedRobot.helpers.scandb import (
get_scan_users, add_scan_user, get_scan_user,
 is_scan_user, remove_scan_user, update_scan_reason, update_scan_proof
)

from InvadedRobot.rank import RANK_USERS

@bot.on_message(filters.command("data",config.COMMANDS))
async def data(_, message):
       reply = message.reply_to_message
       msg = await message.reply_text("`Checking Database...`")
       if not message.from_user.id in (await RANK_USERS()):
            return await msg.edit_text("`Your Don't Have Enough Rights To Get Proof...`")
       elif len(message.command) <2:
            return await msg.edit_text("`Use A Correct Format To Check...`")
       else:
         try:
             user_id = int(message.text.split("-u")[1])
             if (await is_scan_user(user_id)) == False:
                  return await msg.edit_text("`Look's Like This User Was Not Scanned...`")
             else:
                 details = await get_scan_user(user_id)
                 user_id = details["user_id"]
                 reason = details["reason"]
                 date = details["date"]
                 proof = details["proof"]
                 await bot.send_message(message.chat.id, 
                 text=strings.CHECK_TEXT.format(user_id,reason,date),
                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Get Proof",callback_data=f"getproof:{user_id}"),]]),disable_web_page_preview=True)
                 await msg.delete()
         except Exception as e:
              await msg.delete()
              await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=e)

@bot.on_callback_query(filters.regex("getproof"))
async def getproof(_, query):
     user_id = int(query.data.split(":")[1])
     if not query.from_user.id in (await RANK_USERS()):
         await query.answer("Your Don't Have Enough Rights To Get Proof", show_alert=True)
     else:
        try:
           details = await get_scan_user(user_id)
           proof = details["proof"]
           await query.message.reply_document(document=proof, caption=f"**Proof For**: `{user_id}`")
           await query.message.edit_reply_markup(reply_markup=None)
        except Exception as e:
               await query.message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=e)
