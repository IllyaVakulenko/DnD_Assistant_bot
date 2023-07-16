from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard_start = ReplyKeyboardMarkup(
	keyboard=[[KeyboardButton(text="Button")]],
	resize_keyboard=True,
	one_time_keyboard=True,
)