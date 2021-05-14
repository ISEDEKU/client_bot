from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sub = InlineKeyboardMarkup()

BUTTON_1 = 'https://t.me/aparatua'
button_1 = InlineKeyboardButton(text='Подписаться', url=BUTTON_1)
sub.insert(button_1)