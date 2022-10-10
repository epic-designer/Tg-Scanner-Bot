from pyrogram.types import *

HELP_MENU = InlineKeyboardMarkup([[InlineKeyboardButton("𝗥𝗔𝗡𝗞 𝗨𝗦𝗘𝗥𝗦",callback_data="rankusers")
],[InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗥𝗘𝗣𝗢𝗥𝗧",callback_data="how_i_report"),
],[InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗥𝗘𝗩𝗘𝗥𝗧",callback_data="how_i_revert"),
],[InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗦𝗖𝗔𝗡",callback_data="how_i_scan"),
],[InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗖𝗛𝗘𝗖𝗞",callback_data="how_i_check"),
],[InlineKeyboardButton("close Menu",callback_data="how_i_revert")]])
