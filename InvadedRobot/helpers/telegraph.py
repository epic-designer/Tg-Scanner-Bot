from telegraph import upload_file
from InvadedRobot import bot
from pyrogram import filters

async def telegraph(message):
        if not message.reply_to_message and not message.reply_to_message.media:
            return await message.reply_text("`reply to photo or document to upload telegraph note: it file size almost lessen 6mb`")
        else:
           path = await message.reply_to_message.download()
           telegraph = upload_file(path)
           for file_id in telegraph:
               url = "https://telegra.ph" + file_id
           if url.endswith("mp4"):
                return await message.reply_video(video=url,caption=url)
           elif url.endswith("jpg"):
                return await message.reply_photo(photo=url,caption=url)
           elif url.endswith("gif"):
                return await message.reply_animation(animation=url,caption=url)


@bot.on_message(filters.command("tm"))
async def tm(_, message):
       await telegraph(message)
