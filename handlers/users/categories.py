from aiogram import types

from keyboards.inline.category import menu_4
from loader import dp


@dp.message_handler(text='🧾 Категории')
async def categories(message: types.Message):
    await message.answer('Вот все категории', reply_markup=menu_4)