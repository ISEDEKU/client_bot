from aiogram import types

from keyboards.inline.messengers import messenger_button
from loader import dp


@dp.message_handler(text='💭 Мессенджеры')
async def messenger(message: types.Message):
    await message.answer('Вы можете написать нам в . . .', reply_markup=messenger_button)

