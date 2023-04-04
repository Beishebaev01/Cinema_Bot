from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from callback import client_cb
from config import ADMINS
# from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    title = State()
    link = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.chat.id in ADMINS:
        await FSMAdmin.title.set()
        await message.answer("Напишите название фильма.")


async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await FSMAdmin.next()
    await message.answer("Отправьте теперь мне ссылку.")


async def load_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
        await message.answer(f"Название {data['title']}"
                             f"{data['link']}")
    await FSMAdmin.next()
    await message.answer("Всё верно?", reply_markup=client_cb.submit_markup)