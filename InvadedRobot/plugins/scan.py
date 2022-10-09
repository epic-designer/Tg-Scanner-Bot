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

SCAN_TEXT = """
**Scan Processed Time And Date**: `{}`

• **Scanned User**: `{}`
• **Reason**: `{}`
"""

CHECK_TEXT = """
**Details Of Following User:-**

**User Id**: `{}`

**Reason**: 
`{}`

**Scan Processed Time And Date**: `{}`
"""
@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      reply = message.reply_to_message
      date = message.date
      msg = await message.reply_text("`Scanning...`")
      if not message.from_user.id in (await RANK_USERS()):
          return await msg.edit("`You Don't Have Enough Rights To Scan...`")
      elif len(message.command) <2:
          return await msg.edit("`Get Format For Scan By Sending` `/formatting`")
      elif reply:
         try:
            user_id = int(reply.from_user.id)
            reason = message.text.split("-r")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
            if (await is_scan_user(user_id)) == True:
                  await update_scan_reason(user_id,reason)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))
                  await msg.edit("`The Following User Was Already Scanned`\n`So I Have Just Updated The New Details!`")
            else:
                  await add_scan_user(user_id,reason,date)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))
                  await msg.edit("`The Following User Was Successfully Scanned!`")
         except Exception as e:
             await msg.delete()
             await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=e)
      elif not reply:
            try:
               user_id = int(message.text.split("-u")[1].split("-r")[0])
               reason = message.text.split("-r")[1]
               mention = f"[{user_id}](tg://user?id={user_id})"
               if (await is_scan_user(user_id)) == True:
                  await update_scan_reason(user_id,reason)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))
                  await msg.edit("`The Following User Was Already Scanned`\n`So I Have Just Updated The New Details!`")
               else:
                  await add_scan_user(user_id,reason,date)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(date,mention,reason))  
                  await msg.edit("`The Following User Was Successfully Scanned!`")
            except Exception as e:
                  await msg.delete()
                  await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=e)
