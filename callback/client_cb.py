from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

#button_delete = InlineKeyboardButton("УДАЛИТЬ ФИЛЬМ", )


#delete_markup = InlineKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    input_field_placeholder="ВЫБЕРИТЕ ЖЕЛАЕМУЮ ОПЦИЮ"
)

start_button = KeyboardButton("/start")
help_button = KeyboardButton("/help")
button_random = KeyboardButton("/getrandom")
button_all = KeyboardButton("/getfilms")
button_delete = KeyboardButton("/deletefilm")
# button_find = KeyboardButton("/findfilm")


start_markup.add(
    start_button,
    help_button
), start_markup.row(button_random, button_all), start_markup.add(button_delete)

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
