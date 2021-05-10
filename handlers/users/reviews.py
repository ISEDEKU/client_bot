from aiogram import types
from aiogram.utils.markdown import hlink

from keyboards.inline.reviews import reviews_keyboard
from loader import dp


@dp.message_handler(text='🔬 Отзывы')
async def reviews(message: types.Message):
    await  message.answer('Посмотрите отзывы о нас!', reply_markup=reviews_keyboard)

