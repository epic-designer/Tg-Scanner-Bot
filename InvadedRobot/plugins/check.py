import config
import strings

from pyrogram import filters
from pyrogram.types import *
from InvadedRobot import bot
from InvadedRobot.helpers.scansdb import (
get_scan_users, add_scan_user, get_scan_user,
 is_scan_user, remove_scan_user, update_scan_reason, update_scan_proof
)

from NandhaBot.rank import RANK_USERS


@bot.on_message(filters.command("check",config.COMMANDS))
async def check(_, message):
       reply = message.reply_to_message
       msg = await message.reply_text("`checking...`")
       if not message.from_user.id in (await RANK_USERS()):
            return await msg.edit_text("`your don't have enough rights to use me.`")
       elif len(message.command) <2:
            return await msg.edit_text("`use a correct format for check user.`")
       else:
         try:
             user_id = int(message.text.split("-u")[1])
             if (await is_scan_user(user_id)) == False:
                  return await msg.edit_text("`This user not scanned.`")
             else:
                 details = await get_scan_user(user_id)
                 user_id = details["user_id"]
                 reason = details["reason"]
                 date = details["date"]
                 proof = details["proof"]
                 await bot.send_message(message.chat.id, 
                 text=strings.CHECK_TEXT.format(user_id,reason,date),
                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗚𝗘𝗧 𝗣𝗥𝗢𝗢𝗙",callback_data=f"getproof:{user_id}"),]]),disable_web_page_preview=True)
                 await msg.delete()
         except Exception as e:
             await msg.edit_text(str(e))


@bot.on_callback_query(filters.regex("getproof"))
async def getproof(_, query):
     user_id = int(query.data.split(":")[1])
     if not query.from_user.id in (await RANK_USERS()):
         await query.answer("you don't have enough rights to use me.", show_alert=True)
     else:
        try:
           details = await get_scan_user(user_id)
           proof = details["proof"]
           await query.message.reply_document(document=proof, caption=f"proof for: `{user_id}`")
           await query.message.edit_reply_markup(reply_markup=None)
        except Exception as e:
               await query.message.reply_text(str(e))
