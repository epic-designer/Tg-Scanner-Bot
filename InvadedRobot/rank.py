"Function To Get Rank Users For Special Access"
from InvadedRobot.helpers.ranksdb import get_rankusers
from InvadedRobot.helpers.troopsdb import get_troops

async def RANK_USERS():
     list = (await get_rankusers())
     return list

async def TROOP_USERS():
      list = (await get_troops())
      return list
