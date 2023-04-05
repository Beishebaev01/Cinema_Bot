from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from callback import client_cb
from config import ADMINS
from data_base.database import sql_command_insert


class FSMAdmin(StatesGroup):
    title = State()
    link = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.chat.id in ADMINS:
        await FSMAdmin.title.set()
        await message.answer("Напишите название фильма.", reply_markup=client_cb.cancel_markup)


async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await FSMAdmin.next()
    await message.answer("Отправьте теперь мне ссылку.", reply_markup=client_cb.cancel_markup)


async def load_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
        await message.answer(f"{data['title']}"
                             f"{data['link']}")
    await FSMAdmin.next()
    await message.answer("Всё верно?", reply_markup=client_cb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Фильм добавлен!")
    elif message.text == "НЕТ":
        await state.finish()
        await message.answer("Отменено!")
    else:
        await message.answer("Нормально пиши!")


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено!")


def register_handlers_fsm_admin(dp: Dispatcher):
    dp.register_message_handler(cancel, Text(equals="cancel", ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['insert'])
    dp.register_message_handler(load_title, state=FSMAdmin.title)
    dp.register_message_handler(load_link, state=FSMAdmin.link)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
