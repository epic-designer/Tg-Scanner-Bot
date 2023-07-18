import config
import media
from strings import *
import asyncio
import datetime
import time

from InvadedRobot import inv, bot
from InvadedRobot.helpers.status import *
from InvadedRobot.helpers.scandb import *
from pyrogram import *
from pyrogram.types import *

RESTART_TEXT = """
[`SYSTEM AWAKEN`]

📅 DATE: [`{date}`]
⏰ TIME: [`{time}`]
"""

async def railway_to_normal(time_str):
    hour = int(time_str[:2])
    minute = time_str[3:5]
    suffix = "AM" if hour < 12 else "PM"
    hour = hour % 12 if hour != 12 else hour
    return "{}:{} {}".format(hour, minute, suffix)



async def get_datetime():
    timezone = pytz.timezone("Asia/Kolkata")
    kkk = str(datetime.datetime.now(timezone))
    TIME = kkk.split()[1]
    date = kkk.split()[0]
    time = await railway_to_normal(TIME)
    return {"date": date, "time": time}




async def convert_to_datetime(timestamp): # Unix timestamp
     date = datetime.datetime.fromtimestamp(timestamp)
     return date
    

StartTime = time.time()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

 
BUTTON = InlineKeyboardMarkup([[
InlineKeyboardButton("📬",url=config.SYSTEM_CHANNEL_URL),
InlineKeyboardButton("🔊",url=config.GROUP_URL),
InlineKeyboardButton("➕",url=f"t.me/{config.USERNAME}?startgroup=true"),],[
InlineKeyboardButton("🆘 COMMANDS!",callback_data="help"),]])

@bot.on_message(filters.command("start"))
async def start(_, message):
   user_id = message.from_user.id
   if message.chat.type == enums.ChatType.PRIVATE:
     try:
         kk = await message.reply(text="`Analyzing The User`")
         await asyncio.sleep(2)
         await kk.edit(ANI0)
         await asyncio.sleep(1)
         await kk.edit(ANI1)
         await asyncio.sleep(1)
         await kk.edit(ANI2)
         await asyncio.sleep(1)
         await kk.edit(ANI3)
         await asyncio.sleep(1)
         await kk.edit(ANI4)
         await asyncio.sleep(1)
         await kk.edit(ANI5)
         await asyncio.sleep(1)
         await kk.edit(ANI6)
         await asyncio.sleep(1)
         await kk.delete() 
         is_rank = await status(user_id)
         is_scan = await is_scan_user(user_id)
         mention = message.from_user.mention
         await message.reply_photo(media.PM_PHOTO, caption=PM_START_TEXT.format(mention, user_id,is_scan, is_rank),reply_markup=BUTTON)
     except Exception as e:
         await message.reply_photo(photo=(media.ERROR_IMG), caption=f"`{e}`")
   else:
     try:
         if message.chat.username == None:
             await inv.join_chat(message.chat.id)
         else:
             await inv.join_chat(message.chat.username)
         member_count = int(await bot.get_chat_members_count(message.chat.id))
         msg_count = int(await inv.search_messages_count(message.chat.id))
         chat_title = message.chat.title
         chat_id = message.chat.id
         await message.reply_photo(media.PM_PHOTO, caption=GROUP_START_TEXT.format(chat_title,chat_id, member_count,msg_count),reply_markup=BUTTON)
     except Exception as e:
         link = await bot.export_chat_invite_link(message.chat.id)
         await inv.join_chat(link)
         await message.reply_photo(photo=(media.ERROR_IMG), caption=f"`{e}`")
         
@bot.on_callback_query(filters.regex("help"))
async def help(_, query):
    if query.message.media:
         msg = await query.message.edit_caption("`Opening Help Menu...`")
         await asyncio.sleep(2)
         await msg.edit(HELP)
    else:
         msg = await query.message.edit("`Opening Help Menu...`")
         await asyncio.sleep(2)
         await msg.edit(HELP)


async def run_clients():
      await bot.start()
      await inv.start()
      await pyrogram.idle()
      zone = await get_readable_time()
      await bot.send_message(
           chat_id=config.LOG_CHANNEL_ID,
           text=strings.RESTART_TEXT.format(date=zone["date"], time=zone["time"]))
      


if __name__ == "__main__":
    inv.loop.run_until_complete(run_clients())
