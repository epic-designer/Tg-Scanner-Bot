from pyrogram import filters
from pyrogram.types import *

from InvadedRobot import bot

@bot.on_inline_query(filters.regex("ok"))
async def ok(_, query):
    await bot.answer_inline_query(
    query.id,
    results=[
        InlineQueryResultArticle(
            "Ok",
            InputTextMessageContent("Message content"))])
