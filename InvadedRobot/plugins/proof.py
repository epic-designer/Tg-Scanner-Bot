import config

from pyrogram import filters
from pyrogram.types import *
from InvadedRobot import bot
from InvadedRobot.helpers.scandb import (
get_scan_users, add_scan_user, get_scan_user,
 is_scan_user, remove_scan_user, update_scan_reason, update_scan_proof
)

from InvadedRobot.rank import RANK_USERS

@bot.on_message(filters.command("addproof", config.COMMANDS))
async def addproof(_, message):
      reply = message.reply_to_message
      date = message.date
      msg = await message.reply_text("`Adding Proof...`")
      if not message.from_user.id in (await RANK_USERS()):
           return await msg.edit("`You Don't Have Enough Rights To Use Me...`")
      elif len(message.command) <2:
           return await msg.edit("`Use A Correct Format For Adding The Proof...`")
      elif not reply or not reply.media:  
            return await msg.edit("`Reply To A Media To Save Proof...`")
      elif reply:
          try:           
             user_id = int(message.text.split("-u")[1])
             if not user_id in (await get_scan_users()):
                 return await msg.edit("`This User Is Not Scanned The User Must To Been To Add Proof...`")

             await update_scan_proof(user_id, message)
             await msg.edit("`Successfully Added Proof!`")   
          except Exception as e:
              await msg.delete()
              await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")
