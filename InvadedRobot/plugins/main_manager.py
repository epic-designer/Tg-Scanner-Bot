import config
import strings

from pyrogram import *
from pyrogram.types import *
from InvadedRobot import *
from InvadedRobot.helpers.scandb import *
from InvadedRobot.helpers.status import status

from InvadedRobot.rank import *

@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      reply = message.reply_to_message
      date = message.date
      msg = await message.reply_text("`Scanning...`")
      rank = await status(message.from_user.id)
      if not message.from_user.id in (await RANK_USERS()):
          return await msg.edit("`You Don't Have Enough Rights To Scan...`")
      elif len(message.command) <2:
          return await msg.edit("`Get Format For Scan By Sending` `/formatting`")
      elif reply and rank == "Commander" or rank == "Invader":
         try:
            user_id = int(reply.from_user.id)
            reason = message.text.split("-r")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
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
