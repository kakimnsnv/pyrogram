import asyncio, time
from pyrogram import Client
from pyrogram.handlers import MessageHandler

api_id = 28783505 # darthveider_jr
api_hash = "417e398e5a38b5e929cd0ba031e78bcd" #darthveider_jr

# second_api_id = 21892152 # secondAcc
# second_api_hash = "4d3fb91309686cdee3cdd3f218388815" #secondAcc


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        progressholder = 0

        async def my_function(client, message):
            await message.forward("me")

        async def progress(current, total):
            global progressholder
            if current == total:
                await app.send_message("me", "progress is 100%")
        
        async def replySticker(client, message):
            # await app.send_sticker("")
            await message.forward("me")
            await print(client)

        my_handler = MessageHandler(my_function)
        # app.add_handler(my_handler)
        app.add_handler(MessageHandler(replySticker))

        # await app.send_document("me", "0.gif", progress = progress)
        # await app.get_messages("me")
        

asyncio.run(main())