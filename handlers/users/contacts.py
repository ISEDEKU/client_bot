from aiogram import types

from loader import dp


@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(
        'Наши номера телефонов:\n0443322323\n0956956905\n0964304543\n0934162020'
        '\nНаша почта: info@aparat.ua\nНаш сайт: Aparat.ua'
    )