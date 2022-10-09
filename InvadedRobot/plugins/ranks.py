import config
import asyncio

from pyrogram import filters
from pyrogram.types import *


from InvadedRobot import bot
from InvadedRobot.rank import RANK_USERS , TROOP_USERS
from InvadedRobot.helpers.ranksdb import *
from InvadedRobot.helpers.troopsdb import *


@bot.on_message(filters.command("setrank"))
async def rank(_, message):
    reply = message.reply_to_message
    user_id = message.from_user.id
    if not user_id in config.DEVS:
        msg = await message.reply_text("`only devs can access this.`")
        await asyncio.sleep(5)
        await msg.delete()
    elif reply:
           user_id = int(reply.from_user.id)
           if user_id in (await RANK_USER()):
              await message.reply_text("`the user is Invaded you can demote Troops or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("demoet to troops", callback_data=f"demote_to_troops:{user_id}"),],[
InlineKeyboardButton("demoet to troops", callback_data=f"demote_to_civilian:{user_id}")]]))

           elif user_id in (await TROOPS_USERS()):
              await message.reply_text("`the user is Troop you can promote to Invaded or demote to Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("promote to Invaded", callback_data=f"promote_to_invaded:{user_id}"),],[
InlineKeyboardButton("demoet to Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))
           else:
              await message.reply_text("`the user is Civilian you can promote to Invaded or promote to troops`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("promote to Invaded", callback_data=f"promote_to_invaded:{user_id}"),],[
InlineKeyboardButton("demoet to Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))
           

