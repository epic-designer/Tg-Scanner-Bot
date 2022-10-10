from pyrogram.types import *

HELP_MENU_1 = InlineKeyboardMarkup([[InlineKeyboardButton("RANK USER",callback_data="rankusers")
],[InlineKeyboardButton("HOW I REPORT",callback_data="how_i_report"),
],[InlineKeyboardButton("HOW I REVERT",callback_data="how_i_revert"),
],[
InlineKeyboardButton("SKIP HELP",callback_data="help_2"),
InlineKeyboardButton("CLOSE MENU",callback_data="close_menu")]])

HELP_MENU_2 = InlineKeyboardMarkup([[
InlineKeyboardButton("HOW I SCAN",callback_data="how_i_scan"),
],[
InlineKeyboardButton("HOW I CHECK",callback_data="how_i_check"),
],[
InlineKeyboardButton("BACK HELP",callback_data="help_1"),
InlineKeyboardButton("CLOSE MENU",callback_data="close_menu")]])
