from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔍 Поиск'),

        ],
        [
            KeyboardButton(text='📈 Курс'),
            KeyboardButton(text='🔈 Информация'),
            KeyboardButton(text='❓ Помощь')
        ],
    ],
    resize_keyboard=True
)

menu_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✉️ Контакты'),
            KeyboardButton(text='🖥 Сайт'),
            KeyboardButton(text='📎 О нас'),
            KeyboardButton(text='🔬 Отзывы')
        ],
        [
            KeyboardButton(text='💬 Онлайн чат'),
            KeyboardButton(text='🏬 Местоположение'),
            KeyboardButton(text='🧾 Категории')
        ],
        [
            KeyboardButton(text='📱 Соцсети'),
            KeyboardButton(text='🕘 Режим работы'),
            KeyboardButton(text='🔙 Назад')
        ],
    ],
    resize_keyboard=True
)

menu_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❌ Завершить поиск ❌')
        ],
    ],
    resize_keyboard=True
)
