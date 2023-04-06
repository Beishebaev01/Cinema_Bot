from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
# from config import bot
from callback.client_cb import start_markup
from data_base.database import sql_command_random, sql_command_all, sql_command_delete
from parser.parser_from_hdrezka import parser


async def start_command(message: types.Message):
    await message.answer("Здравтвуйте! Я CinemaBot27-1. Могу отправить Вам ссылку на любой фильм\n"
                         "выберите команду", reply_markup=start_markup)


# async def find_film(message: types.Message):
#     await message.answer("Напишите название фильма, чтобы получить его ссылку.")
#     response = message.text
async def delete_films(message: types.Message):
    films = await sql_command_all()
    for film in films:
        await message.answer(
            f"{film[1]}, {film[2]}",
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f"УДАЛИТЬ ФИЛЬМ",
                                                                         callback_data=f"УДАЛИТЬ ФИЛЬМ {film[0]}")))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("УДАЛИТЬ ФИЛЬМ ", ""))
    await call.answer(text="УДАЛЕНО", show_alert=True)
    await call.message.delete()


async def get_films(message: types.Message):
    films = await parser()
    for film in films:
        await message.answer(
            f"<a href='{film['link']}'>{film['title']}</a>\n\n",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(
                    "Перейти", url=film['link']
                )
            ),
            parse_mode=ParseMode.HTML
        )


async def get_random_film(message: types.Message):
    film = await sql_command_random()
    await message.answer(film)


async def help_command(message: types.Message):
    await message.answer("получить один случаный фильм-/getrandom\n"
                         "получить все фильмы из базы данных-/getfilms")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=["help"])
    # dp.register_message_handler(find_film, commands=['findfilm'])
    dp.register_message_handler(get_films, commands=['getfilms'])
    dp.register_message_handler(get_random_film, commands=['getrandom'])
    dp.register_message_handler(delete_films, commands=["deletefilm"])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("УДАЛИТЬ ФИЛЬМ"))
