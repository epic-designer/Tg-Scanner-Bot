import config

from pyrogram import filters
from InvadedRobot import bot
from InvadedRobot.helpers.telegraph import telegraph

@bot.on_message(filters.command(["tm","tgm,"telegraph"],config.COMMANDS))
async def tm(_, message):
       await telegraph(message)

@bot.on_message(filters.command(["formatting","format"],config.COMMANDS))
async def formatting(_, message):
    await message.reply_text(strings.FORMAT_TEXT)
