
from InvadedRobot.rank import RANK_USERS

async def status(user_id: int)
     if user_id in (await RANK_USERS()):
         return "**is Invader**"
     return "**is human**"
