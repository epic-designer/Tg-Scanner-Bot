from pyrogram.types import *

HELP_MENU_1 = InlineKeyboardMarkup([[InlineKeyboardButton("𝗥𝗔𝗡𝗞 𝗨𝗦𝗘𝗥𝗦",callback_data="rankusers")
],[InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗥𝗘𝗣𝗢𝗥𝗧",callback_data="how_i_report"),
],[InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗥𝗘𝗩𝗘𝗥𝗧",callback_data="how_i_revert"),
],[
InlineKeyboardButton("𝗠𝗢𝗥𝗘 𝗛𝗘𝗟𝗣",callback_data="help_2"),
InlineKeyboardButton("𝗖𝗟𝗢𝗦𝗘 𝗠𝗘𝗡𝗨",callback_data="close_menu")]])

HELP_MENU_2 = InlineKeyboardMarkup([[
InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗦𝗖𝗔𝗡",callback_data="how_i_scan"),
],[
InlineKeyboardButton("𝗛𝗢𝗪 𝗜 𝗖𝗛𝗘𝗖𝗞",callback_data="how_i_check"),
],[InlineKeyboardButton("𝗖𝗟𝗢𝗦𝗘 𝗠𝗘𝗡𝗨",callback_data="close_menu")]])
