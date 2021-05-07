from aiogram import types

from loader import dp


@dp.message_handler(text='Режим работы')
async def operating_mode(message: types.Message):
    await message.answer(
        'РЕЖИМ РОБОТИ ІНТЕРНЕТ - МАГАЗИНУ APARAT.UA\nПн-Пт: з 9:00 до 20:00'
        '\nСубота: з 9:00 до 15:00\nНеділя- вихідний'
    )