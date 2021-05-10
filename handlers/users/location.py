from aiogram import types

from keyboards.inline.map import map_location
from loader import dp


@dp.message_handler(text='🏬 Местоположение')
async def location(message: types.Message):
    await message.answer('Вы можете найти нас тут!', reply_markup=map_location)