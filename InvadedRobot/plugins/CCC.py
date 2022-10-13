from pyrogram import filters
from pyrogram.types import *

from InvadedRobot import bot

@bot.on_inline_query(filters.regex("help"))
async def help(_, query):
    await bot.answer_inline_query(
    query.id,
    results=[
        InlineQueryResultArticle(
            "Here the helps!",
            InputTextMessageContent(strings.HELP))])
