from aiogram import types

from loader import dp


@dp.message_handler(text='🏬 Местоположение')
async def location(message: types.Message):
    await message.answer(
        'Мы на карте: https://g.page/aparatua'
    )