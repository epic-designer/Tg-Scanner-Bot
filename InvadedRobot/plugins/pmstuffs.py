import asyncio
import config

from InvadedRobot import bot, inv as ubot
from InvadedRobot.rank import RANK_USERS
from InvadedRobot.rank import RANK_USERS

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters, enums

PM_PHOTO = "https://telegra.ph/file/e9a7b101e8fcc7e6b7381.jpg"
PM_KEYBOARD = [
    [
        InlineKeyboardButton(text="[► Report Error ◄]", url="https://t.me/Aasf_Cyberking"),
        InlineKeyboardButton(text="[► Get Updates ◄]", url="https://t.me/CityOfCreations"),
    ],
    [
        InlineKeyboardButton(text="⊵ Help Guidelines ⊴", callback_data="inv_commands"),
    ],
]
buttons = [
    [
        InlineKeyboardButton(text="[► Report Error ◄]", url="https://t.me/Aasf_Cyberking"),
        InlineKeyboardButton(text="[► Get Updates ◄]", url="https://t.me/CityOfCreations"),
    ],
]

PM_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`

**Invaded Analysis Report :-**
 ➛ **User:** {}
 ➛ **ID:** `{}`
 ➛ **Is Restricted:** `No`
 ➛ **Status:** `{}`
 ➛ **Crime Coefficient:** `Under - 100`
"""

GROUP_START_TEXT = """
`Hello There I Am` `I⊃：INVΛ⊃≡⊃` `The Judgement Enforcing System`

**Invaded Analysis Report :-**
 ➛ **Group:** `{}`
 ➛ **ID:** `{}`
 ➛ **Members Count:** `{}`
 ➛ **Message Count:** `{}`
"""

@bot.on_message(filters.command("start",config.COMMANDS))
async def start(_, m: Message):
    if m.chat.type == enums.ChatType.PRIVATE:
        kk = await m.reply(text="`Analyzing The User`")
        await asyncio.sleep(2)
        mm = await kk.edit_text("`...`")
        await asyncio.sleep(2)
        ll = await mm.edit_text("`Processing...`")
        await asyncio.sleep(3)
        await ll.delete()
    if m.from_user.id in (await RANK_USERS()):
    if m.from_user.id in GODS:
        status = "Invaders"
    elif (await is_scan_user(m.from_user.id)) == True:
        status = "Globally Banned"
    else:
        status = "Civilian"
        await m.reply_photo(
            PM_PHOTO,
            caption=PM_START_TEXT.format(
                m.from_user.mention, m.from_user.id, status
            ),
            reply_markup=InlineKeyboardMarkup(PM_KEYBOARD),
        )
    if not m.chat.type == enums.ChatType.PRIVATE:
     try:
       if m.chat.username == None:
        await ubot.join_chat(m.chat.id)
       else:
        await ubot.join_chat(m.chat.username)
     except Exception:
        link = await bot.export_chat_invite_link(m.chat.id)
        await ubot.join_chat(link)
     try:
        kk = await m.reply(text="`Analyzing The User...`")
        await asyncio.sleep(2)
        await kk.delete()
        count = int(await bot.get_chat_members_count(m.chat.id))
        msgc = int(await ubot.search_messages_count(m.chat.id))
        await m.reply_photo(
            "https://telegra.ph/file/83b667369505a14c8fef2.jpg",
            caption=GROUP_START_TEXT.format(
                m.chat.title,
                m.chat.id,
                count,
                msgc),
                reply_markup=InlineKeyboardMarkup(buttons)
        )
     except Exception as e:
         await m.reply_photo("https://c4.wallpaperflare.com/wallpaper/976/117/318/anime-girls-404-not-found-glowing-eyes-girls-frontline-wallpaper-preview.jpg", caption=f"`404 Error Occurred Failed To Start The Invaded`\n\n `{e}`")
         return
