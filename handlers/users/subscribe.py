from aiogram import types

from keyboards.inline.subscribe import sub
from loader import dp


@dp.message_handler(text='✅ Подписаться')
async def subscribe(message: types.Message):
    await message.answer('Подпишитесь на наш канал, там много интересного!', reply_markup=sub)
