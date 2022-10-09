
import config


from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot
from NandhaBot.helpers.scansdb import (
get_scan_users, add_scan_user, get_scan_user,
 is_scan_user, remove_scan_user, update_scan_reason, update_scan_proof
)

from NandhaBot.rank import RANK_USERS


@bot.on_message(filters.command("addproof",config.COMMANDS))
async def addproof(_, message):
      reply = message.reply_to_message
      date = message.date
      msg = await message.reply_text("`adding proof...`")
      if not message.from_user.id in (await RANK_USERS()):
           return await msg.edit("`you don't have enough rights to use me.`")
      elif len(message.command) <2:
           return await msg.edit("`use a correct format for add proof.`")
      elif not reply or not reply.media:  
            return await msg.edit("`reply to media for save proofs.`")
      elif reply:
          try:           
             user_id = int(message.text.split("-u")[1])
             if not user_id in (await get_scan_users()):
                 return await msg.edit("`this user not a scanned user to add proof.`")

             await update_scan_proof(user_id, message)
             await msg.edit("`Successfully proof added!`")   
          except Exception as e:
              await msg.edit(str(e))
