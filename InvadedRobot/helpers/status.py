import config
from InvadedRobot.rank import RANK_USERS, TROOP_USERS

async def status(user_id: int):
     if user_id in (await RANK_USERS()) and user_id in config.DEVS:
         return "is Invaders"
     if user_id in (await RANK_USERS()):
         return "is Commander"
     if user_id in (await TROOP_USERS()):
         return "is Troops"
     return "is Civilian"
