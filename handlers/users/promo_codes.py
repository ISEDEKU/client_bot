from aiogram import types

from data import config
from loader import dp


@dp.message_handler(text='📜 Промо коды')
async def promo_codes(message: types.Message):
    promo_cods = []
    for promo in config.PROMO_CODES:
        promo_cods.append(promo)
    await message.answer(f'{config.PROMO_TEXT}')
    await message.answer('\n'.join(promo_cods))
