import pyrogram, os, time, asyncio
from pyrogram import Client, filters, idle
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import BotCommand, Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


# api_id = 21892152 # secondAcc
# api_hash = "4d3fb91309686cdee3cdd3f218388815" #secondAcc
api_id = 28783505 # darthveider_jr
api_hash = "417e398e5a38b5e929cd0ba031e78bcd" #darthveider_jr

token = "6266172629:AAFBP9kvV0ck74giGJz3Hxx3R6wNSD-Y0vE"

client = Client("bot_1", api_id, api_hash, parse_mode=pyrogram.enums.ParseMode.HTML)


inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Basic button',
            callback_data='basic_button'
        ),
        InlineKeyboardButton(
            text='Link',
            url="https://kakimnsnv.github.io"
        )
        
    ],
    [
        InlineKeyboardButton(
            text='Profile',
            user_id=688988285
        )
    ]
])

def command_start(client, message):
    message.reply("Hi, You entered start command.", reply_markup=inline_keyboard)

def command_basic(client: Client, call: CallbackQuery):
    call.message.reply(f'You press button with callback_data {call.data}')

def command_run(client, message):
    message.reply("Hi, You entered run or go command.")


client.add_handler(CallbackQueryHandler(command_basic))
client.add_handler(MessageHandler(command_start, filters.command(commands="start")))
client.add_handler(MessageHandler(command_run, filters.command(commands=["run", "go"])))

bot_commands = [
    BotCommand(
        command='start',
        description='Get started'
    ),
    BotCommand(
        command='run',
        description='Launch'
    ),
    BotCommand(
        command='go',
        description='Go to'
    )
]

# client.run()
client.start()
idle()
client.stop()