import config
import strings

from pyrogram import filters
from InvadedRobot import bot, inv
from InvadedRobot.helpers.telegraph import telegraph


@inv.on_message(filters.command(["tm","tgm","telegraph"],config.COMMANDS))
@bot.on_message(filters.command(["tm","tgm","telegraph"],config.COMMANDS))
async def tm(_, message):
       await telegraph(message)

@bot.on_message(filters.command(["formatting","format"],config.COMMANDS))
async def formatting(_, message):
    if message.reply_to_message:
        await message.reply_to_message.reply_photo("https://telegra.ph/file/53da7e9fcba013e63340f.jpg", caption=strings.FORMAT_TEXT)
    else:
       await message.reply_photo("https://telegra.ph/file/53da7e9fcba013e63340f.jpg", caption=strings.FORMAT_TEXT)
