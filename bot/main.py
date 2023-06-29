from aiogram import executor
from bot.src.echobot import dp


executor.start_polling(dp, skip_updates=True)
