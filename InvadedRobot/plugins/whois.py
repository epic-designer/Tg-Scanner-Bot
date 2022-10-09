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

@bot.on_message(filters.command("whois",config.COMMANDS))
async def whois(_, message):
       reply = message.reply_to_message
       msg = await message.reply_text("`Checking Database...`")
       if not message.from_user.id in (await RANK_USERS()):
            return await msg.edit_text("`Your Don't Have Enough Rights To Get Proof...`")
       elif len(message.command) <2 and not message.reply_to_message:
            return await msg.edit_text("`Use A Correct Format To Check...`")
       else:
         try:
             if not message.reply_to_message:
                  user_id = int(message.text.split("-u")[1])
             else:
                  user_id = message.reply_to_message.from_user.id
             if (await is_scan_user(user_id)) == False:
                  data = await bot.get_chat(user_id) 
                  mention = f"[Click Here](tg://user?id={data.id})"
                  text = "**╒═══「 Invaded Results: 」**\n"
                  text += f"**➛ First Name:** `{data.first_name}`\n"
                  text += f"**➛ Last Name:** `{data.last_name}`\n"
                  text += f"**➛ User Id: @{data.id}**\n"
                  text += f"**➛ Username: @{data.username}**\n"
                  text += f"**➛ User Link: {mention}**\n"
                  text += f"**➛ About:** `{data.bio}`\n"
                  return await msg.edit_text(text)
             else:
                 data = await bot.get_chat(user_id) 
                 mention = f"[Click Here](tg://user?id={data.id})"
                 details = await get_scan_user(user_id)
                 user_id = details["user_id"]
                 reason = details["reason"]
                 date = details["date"]
                 proof = details["proof"]
                 text = "**╒═══「 Invaded Results: 」**"
                 text += f"**➛ First Name:** `{data.first_name}`\n"
                 text += f"**➛ Last Name:** `{data.last_name}`\n"
                 text += f"**➛ User Id: @{data.id}**\n"
                 text += f"**➛ Username: @{data.username}**\n"
                 text += f"**➛ User Link: {mention}**\n"
                 text += f"**➛ About:** `{data.bio}`\n"
                 text += f"**➛ Reason:** `{reason}`\n"
                 text += f"**:: Scan Processed Time And Date:** `{date}`\n"
                 await bot.send_message(message.chat.id, text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Get Proof Details",callback_data=f"getproof:{user_id}"),]]),disable_web_page_preview=True)
                 await msg.delete()
         except Exception as e:
              await msg.delete()
              await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")

@bot.on_callback_query(filters.regex("getproof"))
async def getproof(_, query):
     user_id = int(query.data.split(":")[1])
     if not query.from_user.id in (await RANK_USERS()):
         await query.answer("Your Don't Have Enough Rights To Get Proof", show_alert=True)
     else:
        try:
           details = await get_scan_user(user_id)
           proof = details["proof"]
           await query.message.reply_document(document=proof, caption=f"**Proof Details For**: `{user_id}`")
           await query.message.edit_reply_markup(reply_markup=None)
        except Exception as e:
               await query.message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")
