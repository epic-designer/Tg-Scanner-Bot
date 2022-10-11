from telegraph import upload_file
from InvadedRobot.helpers.status import status

async def telegraph(message):
        rank = await status(message.from_user.id)
        if rank == "Civilian":
            return await message.reply_text("`you don't have enough rights to do this.`")
        elif not message.reply_to_message:
            return await message.reply_text("`reply to media to upload telegraph note: it file size almost lessen 6mb`")
        else:
          if message.reply_to_message.sticker:
               path = await message.reply_to_message.download(f"{message.reply_to_message.sticker.file_unique_id}.jpg")
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


