import config
import strings

from InvadedRobot.rank import (
  RANK_USERS, TROOP_USERS)


from InvadedRobot.helpers.scandb import get_scan_users
from InvadedRobot.helpers.status import status
from InvadedRobot import bot


from pyrogram import *

@bot.on_message(filters.command("stats",config.COMMANDS))
async def stats(_, message):
   rank = await status(message.from_user.id)
   if rank == "Civilian":
       return
   else:
       total_scans = len(await get_scan_users())
       total_troop = len(await TROOP_USERS())
       total_commander = len(await RANK_USERS())
       return await message.reply_photo("https://telegra.ph/file/4a5a85404c2d4385daffa.jpg", caption=strings.STATS.format(total_troop,total_commander,total_scans))

@bot.on_message(filters.command("scanlist",config.COMMANDS))
async def scanlist(_, message):
   rank = await status(message.from_user.id)
   if rank == "Civilian":
       return await message.reply("`You Don't Have Enough right To Get List Of Scanned Users.`")
   else:
       try:
          text = "**Here Is The List Of Scanned User Ids**:\n"
          for scan_ids in (await get_scan_users()):
             text += f"➛ `{scan_ids}`\n"
          return await message.reply_photo("https://telegra.ph/file/0d8b5b7cbcc4de9fddd70.jpg", caption=text)
       except MESSAGE_TOO_LONG:
           with io.BytesIO(str.encode(text)) as file:
              file.name = "scanlist.txt"
              await message.reply_document(document=file,caption="`Users List Was Too Long So It Was Sent As Document...`")


