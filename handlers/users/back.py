from aiogram import types

from keyboards.default.main_keyboard import menu_1
from loader import dp


@dp.message_handler(text='🔙 Назад')
async def info(message: types.Message):
    await  message.answer('Возвращаемся обратно', reply_markup=menu_1)
