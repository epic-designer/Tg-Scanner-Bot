import config
import strings

from InvadedRobot.rank import (
  RANK_USERS, TROOP_USERS)


from InvadedRobot.helpers.scandb import get_scan_users
from InvadedRobot.helpers.status import status
from InvadedRobot import bot


from pyrogram import filters

@bot.on_message(filters.command("stats",config.COMMANDS))
async def stats(_, message):
   rank = await status(message.from_user.id)
   if rank == "Civilian":
       return await message.reply("`You Don't have Enough right to Use.`")
   else:
       total_scans = len(await get_scan_users())
       total_troop = len(await TROOP_USERS())
       total_commander = len(await RANK_USERS())
       return await message.reply(strings.STATS.format(total_troop,total_commander,total_scans))
