import config
import strings
import media

from pyrogram import *
from pyrogram.types import *
from InvadedRobot import *
from InvadedRobot.helpers.status import *
from InvadedRobot.helpers.scandb import *

from InvadedRobot.rank import *

@bot.on_message(filters.command("whois",config.COMMANDS))
async def whois(_, message):
       reply = message.reply_to_message
       msg = await message.reply_photo(""https://telegra.ph/file/06a754526911af5baecdf.jpg, "`Checking Database...`")
       rank = await status(message.from_user.id)
       if rank == "Civilian":
            return await msg.edit_text("`Your Don't Have Enough Rights To Get Proof...`")
       elif len(message.command) <2 and not message.reply_to_message:
            return await msg.edit_text("`Reply To A User Or Give An Id To Get Info...`")
       else:
         try:
             if not message.reply_to_message:
                  user_id = int(message.text.split("-u")[1])
             else:
                  user_id = message.reply_to_message.from_user.id
             if (await is_scan_user(user_id)) == False:
                  data = await bot.get_chat(user_id) 
                  is_scan = await is_scan_user(data.id)
                  rank_status = await status(data.id)
                  mention = f"[Click Here](tg://user?id={data.id})"
                  text = "**╒═══「 Invaded Results: 」**\n"
                  text += f"**➛ First Name:** `{data.first_name}`\n"
                  text += f"**➛ Last Name:** `{data.last_name}`\n"
                  text += f"**➛ User Id**: `{data.id}`\n"
                  text += f"**➛ Username: @{data.username}**\n"
                  text += f"**➛ Perm Link: {mention}**\n"
                  text += f"**➛ Status**: `{rank_status}`\n"
                  text += f"**➛ Restricted**: `{is_scan}`\n"
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
                 rank_status = await status(data.id)
                 is_scan = await is_scan_user(data.id)
                 text = "**╒═══「 Invaded Results: 」**\n"
                 text += f"**➛ First Name:** `{data.first_name}`\n"
                 text += f"**➛ Last Name:** `{data.last_name}`\n"
                 text += f"**➛ User Id**: `{data.id}`\n"
                 text += f"**➛ Username: @{data.username}**\n"
                 text += f"**➛ Perm Link: {mention}**\n"
                 text += f"**➛ About:** `{data.bio}`\n"
                 text += f"**➛ Status**: `{rank_status}`\n"
                 text += f"**➛ Restricted**: `{is_scan}`\n\n"
                 text += f"**➛ Reason:** `{reason}`\n"
                 text += f"**: : Scan Processed Time And Date:** `{date}`\n"
                 if proof == None:
                     await msg.delete()
                     await bot.send_message(message.chat.id, text,reply_to_message_id=message.id ,disable_web_page_preview=True)
                 else:
                     await msg.delete()
                     await bot.send_message(message.chat.id, text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Get Proof Details",callback_data=f"getproof:{user_id}"),]]),reply_to_message_id=message.id,disable_web_page_preview=True)
         except Exception as e:
                await msg.delete()
                await message.reply_photo(media.ERROR_IMG, caption=f"`{e}`")
                           
@bot.on_callback_query(filters.regex("getproof"))
async def getproof(_, query):
     user_id = int(query.data.split(":")[1])
     rank = await status(query.from_user.id)
     if rank == "Civilian":
         await query.answer("Your Don't Have Enough Rights To Get Proof", show_alert=True)
     else:
        try:
           details = await get_scan_user(user_id)
           proof = details["proof"]
           await query.message.reply_document(document=proof, caption=f"**Case File For**: `{user_id}`")
           await query.message.edit_reply_markup(reply_markup=None)
        except:
           await query.message.edit("`Sorry Our Commander Scanned Or Approved A Scan Without Adding Proof!`")
