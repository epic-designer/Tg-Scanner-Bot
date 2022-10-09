import config
import strings

from pyrogram import filters
from InvadedRobot import bot

@bot.on_message(filters.command(["formatting","format"],config.COMMANDS))
async def formatting(_, message):
    await message.reply_text(strings.FORMAT_TEXT)
