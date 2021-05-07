from aiogram import types

from keyboards.default.main_keyboard import menu_1
from loader import dp


@dp.message_handler(commands='start')
async def start_search(message: types.Message):
    await message.answer(
        'Привет! Что бы найти какую-нибудь информацию о товаре, нажми "Поиск"\nЕсли хочешь узнать поподробнее, нажми кнопку "Помощь"',
        reply_markup=menu_1)