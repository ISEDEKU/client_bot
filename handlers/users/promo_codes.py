from aiogram import types

from data import config
from loader import dp


@dp.message_handler(text='📜 Промо коды')
async def promo_codes(message: types.Message):
    await message.answer(f'{config.PROMO_CODES}')
