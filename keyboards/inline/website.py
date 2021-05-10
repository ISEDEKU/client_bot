from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

website_url = InlineKeyboardMarkup(row_width=1)

BUTTON_1 = 'https://aparat.ua/o-magazine'
button_1 = InlineKeyboardButton(text='Информация о нас', url=BUTTON_1)
website_url.insert(button_1)

BUTTON_2 = 'https://aparat.ua/informaciya-o-dostavke'
button_2 = InlineKeyboardButton(text='Доставка и оплата', url=BUTTON_2)
website_url.insert(button_2)

BUTTON_3 = 'https://aparat.ua/kontakty'
button_3 = InlineKeyboardButton(text='Контакты', url=BUTTON_3)
website_url.insert(button_3)

BUTTON_4 = 'https://aparat.ua/faq/'
button_4 = InlineKeyboardButton(text='Частые вопросы', url=BUTTON_4)
website_url.insert(button_4)

BUTTON_5 = 'https://aparat.ua/news/'
button_5 = InlineKeyboardButton(text='Новости', url=BUTTON_5)
website_url.insert(button_5)

BUTTON_6 = 'http://apparat.kiev.ua/'
button_6 = InlineKeyboardButton(text='Блог компании', url=BUTTON_6)
website_url.insert(button_6)

BUTTON_7 = 'https://aparat.ua/specials/'
button_7 = InlineKeyboardButton(text='Специальные предложения', url=BUTTON_7)
website_url.insert(button_7)

BUTTON_8 = 'https://aparat.ua/podarochnye-sertifikaty/'
button_8 = InlineKeyboardButton(text='Подарочные сертификаты', url=BUTTON_8)
website_url.insert(button_8)