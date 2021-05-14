from aiogram import types

from keyboards.inline.bot_chat import bot_chat
from loader import dp


@dp.message_handler(text='💬 Онлайн-чат')
async def online_chat(message: types.Message):
    await message.answer('Перейти к онлайн чату по кнопке', reply_markup=bot_chat)

