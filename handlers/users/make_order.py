from aiogram import types

from loader import dp


@dp.message_handler(text='Сделать заказ')
async def make_order(message: types.Message):
    await message.answer(
        'Приймаємо замовлення 24/7:\nhttp://m.me/apparatgps\nhttp://t.me/Aparatua_bot'
    )