from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot_chat = InlineKeyboardMarkup(row_width=1)

BUTTON_1 = 'https://t.me/aparatjivosite_bot?start=666'
button_1 = InlineKeyboardButton(text='Онлай чат', url=BUTTON_1)
bot_chat.insert(button_1)
