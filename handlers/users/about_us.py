from aiogram import types

from loader import dp


@dp.message_handler(text='📎 О нас')
async def about_us(message: types.Message):
    await message.answer(
        '''
Аппаратные решения комфортного досуга\n
Магазин начал свою деятельность в 2007 году. И вот уже более 12 лет мы предлагаем качественную продукцию на территории всей Украины. Аппарат является официальным представителем торговых марок: Garmin, Lowrance, Fusion, Kenwood, Baofeng, Phiradar, Lucky, Humminbird, Falcon, СТЕК.
Мы имеем все необходимые составляющие для полноценного и качественного обслуживания. Обладая широкими познаниями и богатым опытом, высококвалифицированные специалисты готовы предложить консультативную помощь в выборе того или иного интересующего Вас товара/услуги/сервиса. Наши менеджеры всегда помогут выбрать Вам именно те товары, которые отвечают Вашим требованиям.
Наш динамично развивающийся магазин, обладает самым большим ассортиментом товаров навигации, охоты, рыбалки, авто электроники, туристического снаряжения и дополнительных аксессуаров.
        '''
    )
