import os
import config
import logging

from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client
from pymongo import MongoClient

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


#pyrogram bot client start
plugins = dict(root="InvadedRobot")
bot = Client(name=str(config.USERNAME), 
             api_id=config.API_ID, 
             api_hash=config.API_HASH,
             bot_token=config.BOT_TOKEN,
             plugins=plugins)

#pyrogram user Client start
inv = Client(name="Invaded", 
             api_id=config.APP_ID, 
             api_hash=config.APP_HASH,
             session_string=config.SESSION)

#inv.start()

# mongodb from pymongo #
pymongo = MongoClient(config.DB_URL)
pymongodb = pymongo.bot

# mongodb from motor #
mongo = AsyncIOMotorClient(config.DB_URL)
mongodb = mongo.bot 
