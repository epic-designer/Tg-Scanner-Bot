"Rank Users for Special Access"

from InvadedRobot.helpers.ranksdb import get_rankusers

async def RANK_USERS():
     list = (await get_rankusers())
     return list
