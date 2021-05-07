from aiogram import types

from loader import dp


@dp.message_handler()
async def start_search(message: types.Message):
    await message.answer('Простите, но я не отвечаю на обычные собщения.\nМожет быть вы хотели сделать запрос?')

