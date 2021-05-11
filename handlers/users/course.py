from aiogram import types

from keyboards.default.main_keyboard import menu_1
from loader import dp
from parsing.sale import sale_USD


@dp.message_handler(text='📈 Курс')
async def course(message: types.Message):
    await message.answer(f'Актуальный курс на сейчас:\n{sale_USD}', reply_markup=menu_1)
