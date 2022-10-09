import os
import config
import logging

from pyrogram import Client
from pymongo import MongoClient

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

### Add This Vars On Your Deploying App. ###
API_ID = os.environ.get("API_ID", 7126006)
API_HASH = os.environ.get("API_HASH", "f92b05be529835381859ead64a195fa2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5515671520:AAFcuSq058VM8QmShpweRs1p0u0U5pWHIH8")


#pyrogram bot client start

plugins = dict(root="InvadedRobot")
bot = Client(name=str(config.USERNAME), 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=plugins)

# mongodb from pymongo #
pymongo = MongoClient(config.DB_URL)
pymongodb = pymongo.bot
