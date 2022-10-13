import config

from pyrogram import *
from pyrogram.types import *
from InvadedRobot import *
from InvadedRobot.helpers.scandb import *
from InvadedRobot.rank import *

@bot.on_message(filters.command("proof", config.COMMANDS))
async def proof(_, message):
      reply = message.reply_to_message
      date = message.date
      msg = await message.reply_text("`Adding Proof...`")
      if not message.from_user.id in (await RANK_USERS()):
           return
      elif len(message.command) <2:
           return await msg.edit("`Use A Correct Format For Adding The Proof...`")
      elif not reply or not reply.media:  
            return await msg.edit("`Reply To A Media To Save Proof...`")
      elif reply:
          try:           
             user_id = int(message.text.split("-u")[1])
             if not user_id in (await get_scan_users()):
                 return await msg.edit("`This User Is Not Scanned The User Must To Been Scanned To Add Proof...`")

             await update_scan_proof(user_id, message)
             await msg.delete()
             await message.reply_photo("https://telegra.ph/file/fcbfba0b8d16e084b819f.jpg", caption="`Successfully Added Proof!`")   
          except Exception as e:
              await msg.delete()
              await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")
