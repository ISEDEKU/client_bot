from aiogram import types

from keyboards.inline.website import website_url
from loader import dp


@dp.message_handler(text='🖥 Сайт')
async def website(message: types.Message):
    await message.answer('Ссылки на нашем сайте', reply_markup=website_url)
