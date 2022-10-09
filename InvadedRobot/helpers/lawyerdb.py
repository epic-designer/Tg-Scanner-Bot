from InvadedRobot import mongodb

lawyersdb = mongodb.lawyerdb

async def get_lawyers() -> list:

    lawyer_users = await lawyersdb.find_one({"user_id": "user_id"})

    if not lawyer_users:

        return []

    return lawyer_users["lawyer_users"]

async def add_lawyer(user_id: int):

      lawyer_users = await get_lawyers()

      lawyer_users.append(user_id)

      await lawyersdb.update_one(

        {"user_id": "user_id"}, {"$set": {"lawyer_users": lawyer_users}}, upsert=True)

      return True  

async def remove_lawyer(user_id: int):

       lawyer_users = await get_lawyers()

       lwayer_users.remove(user_id)

       await lawyersdb.update_one(

        {"user_id": "user_id"}, {"$set": {"lawyer_users": lawyer_users}}, upsert=True)

       return True
