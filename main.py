import logging
from aiogram.utils import executor
from config import bot, dp, ADMINS
from data_base.database import sql_create, sql_command_random, sql_command_clear
from callback import client
from parser.parser_from_hdrezka import parser
from handlers import fsm_admin


async def on_startup(_):
    await bot.send_message(chat_id=ADMINS[0], text="Я родился!")
    await bot.send_message(chat_id=ADMINS[1], text="Я родился!")
    await bot.send_message(chat_id=ADMINS[2], text="Я родился!")
    await sql_command_clear()
    await parser()
    sql_create()


fsm_admin.register_handlers_fsm_admin(dp)

client.register_handlers_client(dp)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(skip_updates=True, on_startup=on_startup, dispatcher=dp)
