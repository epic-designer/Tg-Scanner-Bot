import config
import media
from InvadedRobot import bot
from pyrogram import filters




if __name__ == "__main__":
     bot.run()
     with bot:
        bot.send_photo(config.LOG_GROUP_ID,photo=media.INVADED_IMG,caption="<b>I'm Awake Already!</b>",
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗚𝗥𝗢𝗨𝗣!",url=f"{config.GROUP_URL}")]]))
