from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category = InlineKeyboardMarkup(row_width=1)

BUTTON_1 = 'https://aparat.ua/turisticheskie-navigatori/'
button_1 = InlineKeyboardButton(text='Туристичні навігатори', url=BUTTON_1)
category.insert(button_1)

BUTTON_2 = 'https://aparat.ua/eholoty-i-kartplottery/'
button_2 = InlineKeyboardButton(text='Ехолоти та картплоттери', url=BUTTON_2)
category.insert(button_2)

BUTTON_3 = 'https://aparat.ua/sport-i-fitnes/'
button_3 = InlineKeyboardButton(text='Аксесуари для спорту та фітнесу', url=BUTTON_3)
category.insert(button_3)

BUTTON_4 = 'https://aparat.ua/gps-navigatory/'
button_4 = InlineKeyboardButton(text='Gps навігатори', url=BUTTON_4)
category.insert(button_4)

BUTTON_5 = 'https://aparat.ua/velosport/'
button_5 = InlineKeyboardButton(text='Велоспорт', url=BUTTON_5)
category.insert(button_5)

BUTTON_6 = 'https://aparat.ua/kamery-i-videoregistratory/'
button_6 = InlineKeyboardButton(text='Камери і Відеореєстратори', url=BUTTON_6)
category.insert(button_6)

BUTTON_7 = 'https://aparat.ua/karti-dlya-navigatorov/'
button_7 = InlineKeyboardButton(text='Карти для GPS Навігаторів', url=BUTTON_7)
category.insert(button_7)

BUTTON_8 = 'https://aparat.ua/aksessuary-dlya-garmin/'
button_8 = InlineKeyboardButton(text='Аксесуари для Garmin', url=BUTTON_8)
category.insert(button_8)

BUTTON_9 = 'https://aparat.ua/drugie-kategorii/'
button_9 = InlineKeyboardButton(text='Каталог товарів', url=BUTTON_9)
category.insert(button_9)





