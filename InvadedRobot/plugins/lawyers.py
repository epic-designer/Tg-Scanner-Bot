from InvadedRobot.rank import RANK_USERS, LAWYERS

from InvadedRobot.helpers.lawyerdb import (
get_lawyers, add_lawyer , remove_lawyer)

RANK_ADDED_TEXT = """
new lawyer user arrived on bot
it's {}
"""
RANK_REMOVED_TEXT = """
the lawyer user remove on bot
it's {}
"""

from InvadedRobot import bot
from pyrogram import filters
from pyrogram.types import *

@bot.on_message(filters.command("addlawyer"))
async def addlawyer(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing adding..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("only the rankusers can add lawyers.")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if user.id in (await LAWYERS()):
               await msg.edit("`your trying add someone that person already a lawyer user`")
           else:
              await add_lawyer(user.id)
              await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if user.id in (await LAWYERS()):
                   await msg.edit("`your trying add someone that person already a lawyer user`")
              else:
                 await add_lawyer(user.id)
                 await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))

@bot.on_message(filters.command("removelawyer"))
async def removelawyer(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing removeing..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("only my rank user can remove lawyers.")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if not user.id in (await LAWYERS()):
               await msg.edit("`your trying remove someone that person is not a lawyer user`")
           else:
              await remove_lawyer(user.id)
              await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if not user.id in (await LAWYERS()):
                   await msg.edit("`your trying remove someone that person is not a lawyer user`")
              else:
                 await remove_lawyer(user.id)
                 await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))


@bot.on_message(filters.command("lawyers"))
async def troopusers(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       msg = await message.reply_text("`getting lawyer users list!`")
       if not user_id in (await LAWYERS()) or not user_id in (await RANK_USERS()):
            await msg.edit_text("`sorry you can't collect lawyers users list.`")
       elif user_id in (await RANK_USERS()) or user_id in (await LAWYERS()):
           LAWYER_USER_TEXT = "𝗟𝗔𝗪𝗬𝗘𝗥𝗦 𝗟𝗜𝗦𝗧:\n\n"
           try:
              for lawyer in (await LAWYERS()):
                   mention = (await bot.get_users(lawyer)).mention
                   LAWYER_USER_TEXT += f"• {mention}\n"
                   await msg.edit(LAWYER_USER_TEXT)
           except Exception as e:
                  await msg.edit(str(e))
