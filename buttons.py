from pyrogram.types import *

HELP_MENU_1 = InlineKeyboardMarkup([[InlineKeyboardButton("Rank Users",callback_data="rankusers")
],[InlineKeyboardButton("How Can I Report",callback_data="how_i_report"),
],[InlineKeyboardButton("How I Revert",callback_data="how_i_revert"),
],[
InlineKeyboardButton("Skip Help",callback_data="help_2"),
InlineKeyboardButton("Close menu",callback_data="close_menu")]])

HELP_MENU_2 = InlineKeyboardMarkup([[
InlineKeyboardButton("How Can I Scan",callback_data="how_i_scan"),
],[
InlineKeyboardButton("How Can I Check",callback_data="how_i_check"),
],[
InlineKeyboardButton("Help Back",callback_data="help_1"),
InlineKeyboardButton("Close Menu",callback_data="close_menu")]])
