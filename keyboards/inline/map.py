from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

map_location = InlineKeyboardMarkup(row_width=1)

BUTTON_1 = 'https://g.page/aparatua'
button_1 = InlineKeyboardButton(text='Карта', url=BUTTON_1)
map_location.insert(button_1)