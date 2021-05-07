from aiogram import types

from keyboards.default.main_keyboard import menu_2
from loader import dp


@dp.message_handler(text='Информация')
async def information(message: types.Message):
    await message.answer('Вот вся информация о нас', reply_markup=menu_2)