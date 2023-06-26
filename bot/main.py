from aiogram import executor
from src.echobot import dp


executor.start_polling(dp, skip_updates=True)
