from aiogram import types
from aiogram.utils.markdown import hlink

from loader import dp


@dp.message_handler(text='💬 Онлайн чат')
async def online_chat(message: types.Message):
    await message.answer(
        hlink('🔵 Telegram 🔵', 'http://t.me/Aparatua_bot') +
        hlink('\n    🟣 Viber 🟣', 'viber://pa?chatURI=aparatua1') +
        hlink('\n🔵 Facebook 🔵', 'http://m.me/apparatgps')
    )
