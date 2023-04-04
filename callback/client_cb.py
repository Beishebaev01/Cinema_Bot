from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")


start_markup.add(
    start_button,
    help_button
)

cancel_button = KeyboardButton("CANCEL")

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    cancel_button
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("НЕТ")
)
