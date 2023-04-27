import asyncio
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

# api_id = 28783505 # darthveider_jr
# api_hash = "417e398e5a38b5e929cd0ba031e78bcd" #darthveider_jr

api_id = 21892152 # secondAcc
api_hash = "4d3fb91309686cdee3cdd3f218388815" #secondAcc

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        async def all_message(client, message):
            await message.reply(message.text)

        myhandler = MessageHandler(all_message)
        app.add_handler(myhandler)
        

asyncio.run(main())