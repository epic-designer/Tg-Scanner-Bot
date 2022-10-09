import config
import strings

from pyrogram import filters
from pyrogram.types import *

from InvadedRobot import bot
from InvadedRobot.helpers.scandb import *
from InvadedRobot.rank import *

@bot.on_message(filters.command("revert",config.COMMANDS))
async def revert(_, message):
      reply = message.reply_to_message
      user_id = message.from_user.id
      msg = await message.reply_text("`reverting scan.`")
      if not user_id in (await RANK_USERS()):
          return msg.edit("`you don't have enough rights to use me.`")
      elif len(message.command) <2:
           return await msg.edit("`use correct format for reverting..`")
      elif reply:
           try:
              user_id = int(reply.from_user.id)
              if (await is_scan_user(user_id)) == False:
                  return await msg.edit("`the user not a scanned user to revert.`")
              else:
                  await remove_scan_user(user_id)
                  await msg.edit("`Successfully revert a user.`") 
                  #bot.send()
           except Exception as e:
                await msg.edit(str(e))
      elif not reply:
             try:
                 user_id = int(message.text.split("-u")[1])
                 if (await is_scan_user(user_id)) == False:
                    return await msg.edit("`the user not a scanned user to revert.`")
                 else:
                      await remove_scan_user(user_id)
                      await msg.edit("`Successfully revert a user.`") 
                      #bot.send()
             except Exception as e:
                    await msg.edit(str(e))

           
