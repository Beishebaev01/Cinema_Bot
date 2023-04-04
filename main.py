import logging
from aiogram.utils import executor
from config import bot, dp, ADMINS
from data_base.database import sql_create
from callback import client


async def on_startup(_):
    await bot.send_message(ADMINS[0], "Я родился!")
    sql_create()


client.register_handlers_client(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(skip_updates=True, on_startup=on_startup, dispatcher=dp)