import config
import asyncio
import media

from pyrogram import *

from pyrogram.types import *

from InvadedRobot import *
from InvadedRobot.rank import *
from InvadedRobot.helpers.ranksdb import *
from InvadedRobot.helpers.troopsdb import *

@bot.on_message(filters.command("rank"))
async def rank(_, message):
    reply = message.reply_to_message
    user_id = message.from_user.id
    if not user_id in config.DEVS:
        msg = await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`Only Invaders Can Access This...`")
        await asyncio.sleep(10)
        await msg.delete()
    elif reply:
       try:
           user_id = int(reply.from_user.id)
           if user_id in (await RANK_USERS()):
              await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`The Following User Is Commander You Can Demote Him Into Troop Or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Demote To Troop", callback_data=f"demote_to_troop:{user_id}"),],[
InlineKeyboardButton("Demote to Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))

           elif user_id in (await TROOP_USERS()):
              await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`The Following User Is Troop You Can Promote Him Into Commander Or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Promote To Commander", callback_data=f"promote_to_commander:{user_id}"),],[
InlineKeyboardButton("Demote To Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))
           else:
              await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`The Following User Is Civilian You Can Promote Him Into Commander Or Troop`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Promote To Commander", callback_data=f"promote_to_commander:{user_id}"),],[
InlineKeyboardButton("Promote To Troop", callback_data=f"promote_to_troop:{user_id}")]]))          
       except Exception as e:
          await message.reply_photo(photo=media.ERROR_IMG,caption=e)
    elif not reply:
       try:
           if len(message.command) <2:
                 msg = await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`You Need To Use Correct Formatting Method...`")
                 await asyncio.sleep(10)
                 await msg.delete() 
           user_id = int(message.text.split("-u")[1])
           if user_id in (await RANK_USERS()):
              await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`The Following User Is Commander You Can Demote Him Into Troop Or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Demote To Troop", callback_data=f"demote_to_troop:{user_id}"),],[
InlineKeyboardButton("Demote To Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))

           elif user_id in (await TROOP_USERS()):
              await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`The Following User Is Troop You Can Promote Him Into Commander Or Demote Him Into Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Promote To Commander", callback_data=f"promote_to_commander:{user_id}"),],[
InlineKeyboardButton("Demote To Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))
           else:
              await message.reply_photo("https://telegra.ph/file/06a754526911af5baecdf.jpg", caption="`The Following User Is Civilian You Can Promote Him Into Commander Or Promote Him InTo Troop`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Promote To Commander", callback_data=f"promote_to_commander:{user_id}"),],[
InlineKeyboardButton("Promote To Troop", callback_data=f"promote_to_troop:{user_id}")]]))           
       except Exception as e:
          await message.reply_photo(photo=media.ERROR_IMG,caption=e)

@bot.on_callback_query(filters.regex("demote_to_civilian"))
async def demote_to_civilian(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only For Invaders", show_alert=True)
      elif user_id in (await RANK_USERS()):
           await remove_rank(user_id)
           await query.message.edit_caption("`Successfully Demoted Commander User Into Civilian!`")
      elif user_id in (await TROOP_USERS()):
           await remove_troop(user_id)
           await query.message.edit_caption("`Successfully Demoted Troop User Into Civilian!`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)

@bot.on_callback_query(filters.regex("demote_to_troop"))
async def demote_to_troop(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only For Invaders", show_alert=True)
      elif user_id in (await RANK_USERS()):
           await remove_rank(user_id)
           await add_troop(user_id)
           await query.message.edit_caption("`Successfully Demoted Commander Into Troop!`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)

@bot.on_callback_query(filters.regex("promote_to_troop"))
async def promote_to_troop(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only For Invaders", show_alert=True)
      else:
           await add_troop(user_id)
           await query.message.edit_caption("`Successfully Promoted Civilian Into Troop!`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)

@bot.on_callback_query(filters.regex("promote_to_commander"))
async def promote_to_commander(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only For Invaders", show_alert=True)
      elif user_id in (await TROOP_USERS()):
            await remove_troop(user_id)
            await add_rank(user_id)
            await query.message.edit_caption("`Successfully Promoted Troop Into Commander`")
      else:
          await add_rank(user_id)
          await query.message.edit_caption("`Successfully Promoted Civilian Into Commander`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)
