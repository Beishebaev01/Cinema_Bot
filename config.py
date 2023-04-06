from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMINS: list =[524696368, 506208514, 1019059760]
