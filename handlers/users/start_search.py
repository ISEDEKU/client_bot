from aiogram import types

from keyboards.default.main_keyboard import menu_3
from loader import dp
from states.state_class import Questions


@dp.message_handler(text='Поиск')
async def start_search(message: types.Message):
    await message.answer('Что нужно найти?', reply_markup=menu_3)
    await Questions.search_name.set()  # запуск первого состояния