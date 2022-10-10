import config
from InvadedRobot.rank import RANK_USERS, TROOP_USERS

async def status(user_id: int):
     if user_id in (await RANK_USERS()) and user_id in config.DEVS:
         return "Invader"
     elif user_id in (await RANK_USERS()):
         return "Commander"
     elif user_id in (await TROOP_USERS()):
         return "Troop"
     return "Civilian"
