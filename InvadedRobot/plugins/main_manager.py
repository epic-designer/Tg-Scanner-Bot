import config
import strings
import media

from pyrogram import *
from pyrogram.types import *
from InvadedRobot import *
from InvadedRobot.helpers.scandb import *
from InvadedRobot.helpers.status import status

from InvadedRobot.rank import *

@bot.on_message(filters.command(["formatting","format"],config.COMMANDS))
async def formatting(_, message):
    await message.reply_text(strings.FORMAT_TEXT)

@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      reply = message.reply_to_message
      date = message.date
      rank = await status(message.from_user.id)
      if rank == "Civilian":
          return await message.reply_text("`You Don't Have Enough Rights To Scan...`")
      elif len(message.command) <2:
          return await message.reply_text("`Get Format For Scan By Sending` `/formatting`")
      elif reply and rank == "Troop":
        try:
            msg = await message.reply_text("`Requesting to Invaded...`")
            user_id = int(reply.from_user.id)
            reason = message.text.split("-r")[1].split("-p")[0]
            proof = message.text.split("-p")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
            if (await is_scan_user(user_id)) == True:
                 await msg.edit("`The user already scanned in Invaded no need request.`")
            else:
                await bot.send_message(config.REPORT_GROUP, text=strings.REQUEST_SCAN.format(message.from_user.mention, mention, reason, proof, date),reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Approve Scan",callback_data=f"approve_scan:{message.from_user.id}:{user_id}:{reason}:{proof}:{date}"),
],[
InlineKeyboardButton("Disapprove Scan",callback_data=f"disapprove_scan:{message.from_user.id}")]]))
                await msg.edit("the user Successfully requested to Invaded")
        except Exception as e:
            await msg.delete()
            await message.reply_photo(media.ERROR_IMG, caption=e)
      elif not reply and rank == "Troop":
        try:
            msg = await message.reply_text("`Requesting to Invaded...`")
            user_id = int(message.text.split("-u")[1].split("-r")[0])
            reason = message.text.split("-r")[1].split("-p")[0]
            proof = message.text.split("-p")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
            if (await is_scan_user(user_id)) == True:
                 await msg.edit("`The user already scanned in Invaded no need request.`")
            else:
                await bot.send_message(config.REPORT_GROUP, text=strings.REQUEST_SCAN.format(message.from_user.mention, mention, reason, proof, date),reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Approve Scan",callback_data=f"approve_scan:{message.from_user.id}:{user_id}:{reason}:{proof}:{date}"),
],[
InlineKeyboardButton("Disapprove Scan",callback_data=f"disapprove_scan:{message.from_user.id}")]]))
                await msg.edit("the user Successfully requested to Invaded")
        except Exception as e:
            await msg.delete()
            await message.reply_photo(media.ERROR_IMG, caption=e)
      elif reply and rank == "Commander" or rank == "Invader":
         try:
            user_id = int(reply.from_user.id)
            reason = message.text.split("-r")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
            msg = await message.reply_text("`Scanning...`")
            if (await is_scan_user(user_id)) == True:
                  await update_scan_reason(user_id,reason)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(message.from_user.id,mention,reason,date))
                  await msg.edit("`The Following User Was Already Scanned`\n`So I Have Just Updated The New Details!`")
            else:
                  await add_scan_user(user_id,reason,date)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(message.from_user.id,mention,reason,date))
                  await msg.edit("`The Following User Was Successfully Scanned!`")
         except Exception as e:
             await msg.delete()
             await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")
      elif not reply and rank == "Commander" or rank == "Invader":
            try:
               user_id = int(message.text.split("-u")[1].split("-r")[0])
               reason = message.text.split("-r")[1]
               mention = f"[{user_id}](tg://user?id={user_id})"
               msg = await message.reply_text("`Scanning...`")
               if (await is_scan_user(user_id)) == True:
                  await update_scan_reason(user_id,reason)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(message.from_user.id,mention,reason,date))
                  await msg.edit("`The Following User Was Already Scanned`\n`So I Have Just Updated The New Details!`")
               else:
                  await add_scan_user(user_id,reason,date)
                  await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_TEXT.format(message.from_user.id,mention,reason,date))
                  await msg.edit("`The Following User Was Successfully Scanned!`")
            except Exception as e:
                  await msg.delete()
                  await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")



@bot.callback_query(filters.regex("approve_scan"))
async def approve_scan(_, query):
     troop_user_id = int(query.data.split(":")[1])
     scan_user_id = int(query.data.split(":")[2])
     reason = query.data.split(":")[3]
     proof = query.data.split(":")[4]
     date = query.data.split(":")[5]
     rank = await status(query.from_user.id)
     try:
       if rank == "Civilian":
          return await query.answer("You don't have enough rights!", show_alert=True)
       elif (await is_scan_user(scan_user_id)) == True:
           return await query.answer("This User Already Scanned!", show_alert=True)
       else:
           await add_scan_user(scan_user_id, reason, date)
           await query.message.edit(f"`the scan was approved but you need to add proof manually here the proof link:``{proof}`")
     except Exception as e:
          await query.message.reply_photo(media.ERROR_IMG,caption=str(e))
        



         









@bot.on_message(filters.command("revert",config.COMMANDS))
async def revert(_, message):
      reply = message.reply_to_message
      user_id = message.from_user.id
      msg = await message.reply_text("`Reverting Scan...`")
      if not user_id in (await RANK_USERS()):
          return await msg.edit("`You Don't Have Enough Rights To Scan...`")
      elif reply:
           try:
              user_id = int(reply.from_user.id)
              if (await is_scan_user(user_id)) == False:
                  return await msg.edit("`The Following User Is Not A Scanned User How Can I Revert A User's Scan Who Wasn't Scanned ?`")
              else:
                  await remove_scan_user(user_id)
                  await msg.edit("`Successfully Reverted A Scan Of The User...`") 
                  #bot.send()
           except Exception as e:
                await msg.delete()
                await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")
      elif not reply:
             try:
                 user_id = int(message.text.split("-u")[1])
                 if (await is_scan_user(user_id)) == False:
                    return await msg.edit("`The Following User Is Not A Scanned User How Can I Revert A User's Scan Who Wasn't Scanned ?`")
                 else:
                      await remove_scan_user(user_id)
                      await msg.edit("`Successfully Reverted A Scan Of The User...`") 
                      #bot.send()
             except Exception as e:
                await msg.delete()
                await message.reply_photo("https://telegra.ph/file/f21e5445b3d0897f63f3d.jpg", caption=f"`{e}`")
