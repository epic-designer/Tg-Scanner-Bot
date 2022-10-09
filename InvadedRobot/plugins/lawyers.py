from InvadedRobot.rank import RANK_USERS, troopS

from InvadedRobot.helpers.troopdb import (
get_troops, add_troop, remove_troop)

RANK_ADDED_TEXT = """
new troopuser arrived on bot
it's {}
"""
RANK_REMOVED_TEXT = """
the troopuser remove on bot
it's {}
"""

from InvadedRobot import bot
from pyrogram import filters
from pyrogram.types import *

@bot.on_message(filters.command("addtroop"))
async def addtroop(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing adding..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("only the rankusers can add troops.")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if user.id in (await troopS()):
               await msg.edit("`your trying add someone that person already a troopuser`")
           else:
              await add_troop(user.id)
              await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if user.id in (await troopS()):
                   await msg.edit("`your trying add someone that person already a troopuser`")
              else:
                 await add_troop(user.id)
                 await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))

@bot.on_message(filters.command("removetroop"))
async def removetroop(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing removeing..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("only my rank user can remove troops.")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if not user.id in (await troopS()):
               await msg.edit("`your trying remove someone that person is not a troopuser`")
           else:
              await remove_troop(user.id)
              await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if not user.id in (await troopS()):
                   await msg.edit("`your trying remove someone that person is not a troopuser`")
              else:
                 await remove_troop(user.id)
                 await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))


@bot.on_message(filters.command("troops"))
async def troopusers(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       msg = await message.reply_text("`getting troopusers list!`")
       if not user_id in (await troopS()) or not user_id in (await RANK_USERS()):
            await msg.edit_text("`sorry you can't collect troops users list.`")
       elif user_id in (await RANK_USERS()) or user_id in (await troopS()):
           troop_USER_TEXT = "𝗟𝗔𝗪𝗬𝗘𝗥𝗦 𝗟𝗜𝗦𝗧:\n\n"
           try:
              for troopin (await troopS()):
                   mention = (await bot.get_users(troop)).mention
                   troop_USER_TEXT += f"• {mention}\n"
                   await msg.edit(troop_USER_TEXT)
           except Exception as e:
                  await msg.edit(str(e))
