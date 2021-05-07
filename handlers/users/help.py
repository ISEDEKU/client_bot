from aiogram import types

from keyboards.default.main_keyboard import menu_1
from loader import dp


@dp.message_handler(text='Помощь')
async def start_search(message: types.Message):
    await message.answer('''
Я бот, который помогает найти информацию о товаре!\n
Чтобы начть поиск, нажмите кнопку "Поиск", затем введите название искомого товара.
Вам не обязательно вводить название или атрибут целиком, в таком случае я выведу вам список товаров.\n
Что бы узнать курс для покупки USD нажмите кнопку "Курс"\n
Нажав кнопку "Информация" вы можете познакомиться с нами поближе!
''', reply_markup=menu_1)
