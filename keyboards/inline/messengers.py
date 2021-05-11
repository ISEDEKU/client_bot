from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

messenger_button = InlineKeyboardMarkup(row_width=3)

BUTTON_1 = 'http://t.me/aparatjivosite_bot'
button_1 = InlineKeyboardButton(text='Telegram', url=BUTTON_1)
messenger_button.insert(button_1)

# BUTTON_2 = 'viber://pa?chatURI=aparat1'
# button_2 = InlineKeyboardButton(text='Viber', url=BUTTON_2)
# messenger_button.insert(button_2)

BUTTON_3 = 'http://m.me/apparatgps'
button_3 = InlineKeyboardButton(text='Facebook', url=BUTTON_3)
messenger_button.insert(button_3)
