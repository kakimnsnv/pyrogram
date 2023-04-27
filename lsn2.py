import pyrogram, time
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatAction


# api_id = 21892152 # secondAcc
# api_hash = "4d3fb91309686cdee3cdd3f218388815" #secondAcc
api_id = 28783505 # darthveider_jr
api_hash = "417e398e5a38b5e929cd0ba031e78bcd" #darthveider_jr

client = Client("me_client", api_id= api_id, api_hash= api_hash, parse_mode=ParseMode.HTML)

# media = []

# @client.on_message(filters=pyrogram.filters.media_group)
# def all_message(client: Client, message: Message):
#     if message.media_group_id in media:
#         return
#     media.append(message.media_group_id)
#     message.reply("You send a mediagroup", quote=True)
    
    # client.send_message("me", message.chat.id)



client.start()
for i in range(1, 101):
    client.send_message(589407608, f"Жан, ты көтенбоқ")
client.stop()


# client.run()