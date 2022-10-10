from InvadedRobot import bot
from pyrogram import filters 
from PIL import Image, ImageDraw, ImageFont
import os
import random
import requests 
import io
from io import BytesIO


@bot.on_message(filters.command("get_id"))
async def image_maker(_, message) -> None:
    # Download profile photo
    await bot.download_media(
        message.reply_to_message.from_user.photo.big_file_id, file="user.png", download_big=True
    )
    k = ["https://telegra.ph/file/853962e208ec379284185.jpg", "https://telegra.ph/file/dd9a03db6d6f7cd577ad0.jpg"]
    y = random.choice(k)
    # open id photo
    id_template = Image.open(io.BytesIO(requests.get(y).content))
    # resize user photo to fit box in id template
    user_photo = user_photo.resize((1159, 1241))
    # put image in position
    id_template.paste(user_photo, (1003, 641))
    # postion on where to draw text
    draw = ImageDraw.Draw(id_template)
    color = "rgb(0, 0, 0)"  # black
    font = ImageFont.truetype("font.ttf", size=80)
    font2 = ImageFont.truetype("font2.ttf", size=100)
    # put text in image
    draw.text(
        (1000, 460),
        message.reply_to_message.from_user.first_name.replace("\u2060", ""),
        fill=color,
        font=font2,
    )
    draw.text((393, 50), str(message.reply_to_message.from_user.id), fill=color, font=font)
    id_template.save("user_id.png")
    await bot.send_file(
        message.chat.id,
        file="user_id.png",
        caption="Generated User ID"
    )
    os.remove("user_id.png")
