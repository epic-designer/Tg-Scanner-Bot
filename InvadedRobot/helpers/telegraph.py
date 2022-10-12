from telegraph import upload_file
from InvadedRobot.helpers.status import status
from datetime import datetime

async def telegraph(message):
        rank = await status(message.from_user.id)
        if rank == "Civilian":
            return 
        elif not message.reply_to_message:
            return await message.reply_text("`Reply To A Media To Get Telegraph Link`\n\n**Note:-** `The Following Media You Have Reply Must Been Less Than 6mb`")
        start = datetime.now()
        path = await message.reply_to_message.download()
        telegraph = upload_file(path)
        for file_id in telegraph:
            url = "https://telegra.ph" + file_id
            end = datetime.now()
        ms = (end - start).seconds
        caption = f"**dl speed**: `{ms}`\n\n{url}"
        if url.endswith("mp4"):
                return await message.reply_video(video=url,caption=caption)
        elif url.endswith("jpg"):
                return await message.reply_photo(photo=url,caption=caption)
        elif url.endswith("gif"):
                return await message.reply_animation(animation=url,caption=caption)


