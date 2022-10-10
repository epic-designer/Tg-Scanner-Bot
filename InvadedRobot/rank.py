from InvadedRobot.helpers.ranksdb import *
from InvadedRobot.helpers.troopsdb import *

async def RANK_USERS():
     list = (await get_rankusers())
     return list

async def TROOP_USERS():
      list = (await get_troops())
      return list
