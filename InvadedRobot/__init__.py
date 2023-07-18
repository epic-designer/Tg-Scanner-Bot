import os
import config
import logging

from motor.motor_asyncio import *
from pyrogram import *
from pymongo import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# PYROGRAM USER CLIENT 
inv = Client(name="katsuki", session_string=config.SESSION, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="InvadedRobot"))

#PYROGRAM BOT CLIENT
bot = Client(name="KatsukiBot", bot_token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH, plugins=dict(root="InvadedRobot"))

pymongo = MongoClient(config.DB_URL)
pymongodb = pymongo.bot

mongo = AsyncIOMotorClient(config.DB_URL)
mongodb = mongo.bot 

class INFO:
   def inv():
      info = app.get_me()
      return info   
     
   def bot():
      info = bot.get_me()
      return info
