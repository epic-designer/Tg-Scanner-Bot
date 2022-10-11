



async def admin(chat_id: int, user_id: int):
       admin = await bot.get_chat_member(chat_id, user_id)
       if admin.privileges:
           return True
       return False
