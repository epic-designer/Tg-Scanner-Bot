import config
import strings
import media

from pyrogram import *
from pyrogram.types import *
from InvadedRobot import *
from InvadedRobot.helpers.scandb import *
from InvadedRobot.helpers.status import *

from InvadedRobot.rank import *

@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      global date, req_msg
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
                 await msg.edit("`The Following User Is Already Scanned In System No Need To Request Scan`")
            else:
                troop_id = message.from_user.id
                await bot.send_message(config.REPORT_GROUP, text=strings.REQUEST_SCAN.format(message.from_user.mention, mention, reason, proof, date),reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Approve Scan",callback_data=f"approve_scan:{user_id}:{reason}:{proof}:{troop_id}"),
],[
InlineKeyboardButton("Disapprove Scan",callback_data=f"disapprove_scan:{user_id}:{troop_id}")]]))
                await msg.delete()
                req_msg = await message.reply_text("`The Request Successfully Sent To Invaded`")
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
            uid = message.from_user.id
            if (await is_scan_user(user_id)) == True:
                 await msg.edit("`The Following User Is Already Scanned In System No Need To Request Scan`")
            else:
                troop_id = message.from_user.id
                await bot.send_message(config.REPORT_GROUP, text=strings.REQUEST_SCAN.format(message.from_user.mention, mention, reason, proof, date),reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Approve Scan",callback_data=f"approve_scan:{user_id}:{reason}:{proof}:{troop_id}"),
],[
InlineKeyboardButton("Disapprove Scan",callback_data=f"disapprove_scan:{user_id}:{troop_id}")]]))
                await msg.delete()
                req_msg = await message.reply_text("`The Request Successfully Sent To Invaded`")
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

@bot.on_callback_query(filters.regex("approve_scan"))
async def approve_scan(_, query):
     scan_user_id = int(query.data.split(":")[1])
     reason = query.data.split(":")[2]
     proof = query.data.split(":")[3]
     troop_user_id = query.data.split(":")[4]
     rank = await status(query.from_user.id)
     scan_user_mention = f"[{scan_user_id}](tg://user?id={scan_user_id})"
     troop_user_mention = f"[{troop_user_id}](tg://user?id={troop_user_id})"
     approved_user_mention = f"[{query.from_user.id}](tg://user?id={query.from_user.id})"
     try:
       if rank == "Civilian" or rank == "Troop":
            return await query.answer("You Don't Have Enough Rights!", show_alert=True)
       elif (await is_scan_user(scan_user_id)) == True:
            return await query.answer("This User Already Scanned!", show_alert=True)
       else:
           await add_scan_user(scan_user_id, reason, date)
           await query.message.edit(f"`The Scan Was Successfully Approved But You Need To Add Proof Manually Here Is The Proof Link:``{proof}`")
           await bot.send_message(config.LOG_CHANNEL_ID, text=strings.SCAN_APPROVED.format(troop_user_mention,scan_user_mention,approved_user_mention,reason,date))
           await req_msg.edit("`Your Request Is Successfully Approved By Commander`")
     except Exception as e:
          await query.message.reply_photo(media.ERROR_IMG,caption=str(e))

@bot.on_callback_query(filters.regex("disapprove_scan"))
async def disapprove_scan(_, query):
     scan_user_id = int(query.data.split(":")[1])
     troop_user_id = query.data.split(":")[2]
     rank = await status(query.from_user.id)
     try:
       if rank == "Civilian" or rank == "Troop":
            return await query.answer("You Don't Have Enough Rights!", show_alert=True)
       elif (await is_scan_user(scan_user_id)) == True:
            return await query.answer("This User Already Scanned!", show_alert=True)
       else:
           await query.message.edit("`The Scan Was Successfully Disapproved`")
           await bot.send_message(troop_user_id, text=strings.SCAN_DISAPPROVED.format(scan_user_id))
           await req_msg.edit("`Your Request Is Successfully Disapproved By Commander Try Scanning Again With Proper Proof And Reason`")
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
