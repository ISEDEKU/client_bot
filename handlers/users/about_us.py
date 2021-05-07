from aiogram import types

from loader import dp


@dp.message_handler(text='О нас')
async def about_us(message: types.Message):
    await message.answer(
        'Компанія Аппарат\nКоманда, Сертифікати та Переваги Інтернет Магазину | aparat.ua'
        '\nКоманда Сертифікати та Переваги інтернет-магазин aparat.ua :heavy_check_mark:Проверенное Якість ?'
        '\nДоступние ціни :airplane:Бистрая доставка в усі регіони України.'
        '\nТелефонуйте :phone: 0956956905 :phone: 0964304543'
        '\n\nЧто бы найти какую-нибудь информацию о товаре, нажми "Поиск"\nЕсли хочешь узнать поподробнее, нажми кнопку "Помощь"', )
