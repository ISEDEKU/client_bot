from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

soc_net_keyboard = InlineKeyboardMarkup(row_width=1)

BUTTON_1 = 'https://www.facebook.com/apparatgps'
button_1 = InlineKeyboardButton(text='Мы в Facebook', url=BUTTON_1)
soc_net_keyboard.insert(button_1)

BUTTON_2 = 'https://www.instagram.com/aparat.ua'
button_2 = InlineKeyboardButton(text='Мы в Instagram', url=BUTTON_2)
soc_net_keyboard.insert(button_2)

BUTTON_3 = 'https://www.youtube.com/apparatkievua'
button_3 = InlineKeyboardButton(text='Мы на Youtube', url=BUTTON_3)
soc_net_keyboard.insert(button_3)

BUTTON_4 = 'https://t.me/aparatua'
button_4 = InlineKeyboardButton(text='Мы в Telegram', url=BUTTON_4)
soc_net_keyboard.insert(button_4)