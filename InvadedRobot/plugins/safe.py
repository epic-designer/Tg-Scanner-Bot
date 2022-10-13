import os
import sys
import config
import subprocess
import asyncio 

from InvadedRobot import *
from pyrogram import *

@bot.on_message(filters.user(config.DEVS) & filters.command("gitpull",config.COMMANDS) & ~filters.forwarded)
async def gitpull(_, message):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await message.reply_photo("https://telegra.ph/file/720363b6527dc4cfbe989.jpg", caption="`Git Pulled Probably`")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)

@bot.on_message(filters.user(config.DEVS) & filters.command("restart",config.COMMANDS) & ~filters.forwarded)
async def restart(_, message):
    k = await message.reply_photo("https://telegra.ph/file/e9921cfaf2d082eee7407.jpg", caption="`Restarting...`")
    await bot.stop()
    await inv.stop()
    await asyncio.sleep(2)
    await inv.run()
    await bot.run()
    await k.edit_caption("`Restarted Successfully!!!`")

@bot.on_message(filters.user(config.DEVS) & filters.command("shutdown",config.COMMANDS) & ~filters.forwarded)
async def shutdown(event):
    k = await message.reply_photo("https://telegra.ph/file/180353501a3a40c052010.jpg", caption="`Shutting Down...`")
    await asyncio.sleep(2)
    await k.edit_caption("`Shut Downed Successfully`")
    await bot.stop()
    await inv.stop()
