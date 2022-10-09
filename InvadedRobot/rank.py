"Function To Get Rank Users For Special Access"
from InvadedRobot.helpers.ranksdb import get_rankusers
from InvadedRobot.helpers.lawyerdb import get_lawyers

async def RANK_USERS():
     list = (await get_rankusers())
     return list
async def LAWYERS():
      list = (await get_lawyers())
      return list
