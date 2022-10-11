



async def admin(user_id: int):
       admin = await get_member(user_id)
       if admin.privileges:
           return True
       return False
