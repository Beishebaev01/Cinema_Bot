from aiogram import types, Dispatcher
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
# from config import bot
# from keyboards.client_cb import start_markup
# from database.bot_db import sql_command_random
# from parser.my_git import parser


async def start_command(message: types.Message):
    await message.answer("Здравтвуйте! Я CinemaBot27-1. Могу отправить Вам ссылку на любой фильм"
                         "\n/help - Помощь")


async def help_command(message: types.Message):
    await message.answer("Напишите название фильма, чтобы получить его ссылку.")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])