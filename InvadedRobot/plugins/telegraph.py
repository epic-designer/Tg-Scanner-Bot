import config

from pyrogram import filters
from InvadedRobot import bot, inv
from InvadedRobot.helpers.telegraph import telegraph


@inv.on_message(filters.command(["tm","tgm","telegraph"],config.COMMANDS))
@bot.on_message(filters.command(["tm","tgm","telegraph"],config.COMMANDS))
async def tm(_, message):
       await telegraph(message)
