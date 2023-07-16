from os import getenv
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, types, executor
from keyboards import *


# Load environment variables from .env file
load_dotenv()
TELEGRAM_TOKEN = getenv("TOKEN")

# Bot and Dispatcher initialization
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    
    await message.reply("Hello! I am your DM assistant in DnD!", reply_markup=keyboard_start)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    # Here you can implement the logic for handling text messages
    await message.reply("I don't know what to do with this message yet.")

# Starting the bot
if __name__ == '__main__':
    # Logging configuration
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
