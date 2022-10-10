import os
import sys
import config
import subprocess

from InvadedRobot import *
from pyrogram import *

@bot.on_message(filters.user(config.DEVS) & filters.command("gitpull",config.COMMANDS) & ~filters.forwarded)
async def gitpull(_, message):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await message.reply_text("`Git Pulled Probably`")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)

@bot.on_message(filters.user(config.DEVS) & filters.command("restart",config.COMMANDS) & ~filters.forwarded)
async def restart(_, message):
    k = await message.reply_text("`Restarting...`")
    await bot.restart()
    await inv.restart()
    os.execl(sys.executable, sys.executable, *sys.argv)
    sys.exit()
    await k.edit("`Restarted Successfully!!!`")

@bot.on_message(filters.user(config.DEVS) & filters.command("shutdown",config.COMMANDS) & ~filters.forwarded)
async def shutdown(event):
    await message.reply_text("`Shutting Down...`")
    await bot.disconnect()
    await inv.disconnect()
