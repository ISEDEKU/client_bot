from aiogram import types

from loader import dp


@dp.message_handler(text='🧾 Категории')
async def categories(message: types.Message):
    await message.answer(
        'Туристичні навігатори:\nhttps://aparat.ua/turisticheskie-navigatori/'
        '\nЕхолоти та картплоттери:\nhttps://aparat.ua/eholoty-i-kartplottery/'
        '\nАксесуари для спорту та фітнесу:'
        '\nhttps://aparat.ua/sport-i-fitnes/'
        '\nGps навігатори:\nhttps://aparat.ua/gps-navigatory/'
        '\nВелоспорт:\nhttps://aparat.ua/velosport/'
        '\nКамери і Відеореєстратори:\nhttps://aparat.ua/kamery-i-videoregistratory/'
        '\nКарти для GPS Навігаторів:\nhttps://aparat.ua/karti-dlya-navigatorov/'
        '\nАксесуари для Garmin:\nhttps://aparat.ua/aksessuary-dlya-garmin/'
        '\nКаталог товарів:\nhttps://aparat.ua/drugie-kategorii/'
        '\nКомпанія Аппарат:\nКупити Туристичні Навігатори в Києві. Порівняти Ціни по Україні | aparat.ua'
        '\nКупуйте Туристичні GPS Навігатори в інтернет-магазин aparat.ua ?100% Оригінал :heavy_check_mark:'
        'Проверенное Якість ?Доступние ціни :airplane:Бистрая доставка в усі регіони Укра...'
        '\nhttps://aparat.ua/servisnye-tsentry">Сервісні центри'
        '\nhttps://aparat.ua/ustanovka-kart">Установка карт'
        '\nhttps://aparat.ua/remont-navigatorov">Ремонт навігаторів'
        '\nhttps://aparat.ua/remont-chasov-i-brasletov-garmin">Ремонт годинників та браслетів Garmin'
        '\nhttps://aparat.ua/ustanovka-oborudovaniya">Встановлення обладнання'
        '\nhttps://aparat.ua/trade-in-prokachaj-svoj-staryj-navigator-ili-chasy-na-novyj">Послуга Trade-in'
        '\nКомпанія Аппарат:'
        '\nСервісний центри Garmin (Гармін). Офіційний сервіс Гармін (Garmin) | aparat.ua'
        '\n?Сервісний центри Garmin? Купуйте >Звоніте :phone: 0956956905 :phone: 0964304543 :heavy_check_mark:'
        'Лучшая Ціна :heavy_check_mark:Офіціальная Гарантія :airplane:Прайс на Послуги'
        '\nВідгуки Facebook:'
        '\nhttps://www.facebook.com/apparatgps/reviews/'
        '\nВідгуки Google:'
        '\nhttps://www.google.com/search?q=отзывы+aparat.ua&sxsrf=ALeKk00oYaqBfhw3L8C50XF0ml2ZiUy_'
        'DA:1617353061189&ei=ZdlmYMj2Cs39rgTNl7yADQ&oq=отзывы+aparat.ua&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBgg'
        'AEAgQHjoHCCMQsAMQJ1D7iwFY948BYNuTAWgBcAB4AIABqgGIAcMCkgEDMi4xmAEAoAEBqgEHZ3dzLXdpesgBAcABAQ&sclient='
        'gws-wiz&ved=0ahUKEwiIvcDVld_vAhXNvosKHc0LD9AQ4dUDCA0&uact=5', disable_web_page_preview=True
    )