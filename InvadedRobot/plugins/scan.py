import config
import strings

from pyrogram import filters
from pyrogram.types import *
from InvadedRobot import bot
from InvadedRobot.helpers.scandb import (
get_scan_users, add_scan_user, get_scan_user,
 is_scan_user, remove_scan_user, update_scan_reason, update_scan_proof
)

from NandhaBot.rank import RANK_USERS


SCAN_TEXT = """
which date this 
scan process: {}

scanned user: {}
reason: {}
"""

CHECK_TEXT = """
𝗦𝗖𝗔𝗡𝗡𝗘𝗗 𝗨𝗦𝗘𝗥:

**ID**: `{}`

**REASON**: 
`{}`

**SCAN DATE**: `{}`
"""
@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      reply = message.reply_to_message
      date = message.date
      msg = await message.reply_text("`scanning....`")
      if not message.from_user.id in (await RANK_USERS()):
          return await msg.edit("`you don't have enough rights to use me.`")
      elif len(message.command) <2:
          return await msg.edit("`you need to use correct `/formatting` for scanning someone else.`")
      elif reply:
         try:
            user_id = int(reply.from_user.id)
            reason = message.text.split("-r")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
            if (await is_scan_user(user_id)) == True:
                  await update_scan_reason(user_id,reason)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))
                  await msg.edit("`the user already scanned.\nI have updated the details!`")
            else:
                  await add_scan_user(user_id,reason,date)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))
                  await msg.edit("`the user successfully scanned!`")
         except Exception as e:
             await msg.edit(str(e))
      elif not reply:
            try:
               user_id = int(message.text.split("-u")[1].split("-r")[0])
               reason = message.text.split("-r")[1]
               mention = f"[{user_id}](tg://user?id={user_id})"
               if (await is_scan_user(user_id)) == True:
                  await update_scan_reason(user_id,reason)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))
                  await msg.edit("`the user already scanned.\nI have updated the details!`")
               else:
                  await add_scan_user(user_id,reason,date)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))  
                  await msg.edit("`the user successfully scanned!`")            
            except Exception as e:
               await msg.edit(str(e))
      
      
