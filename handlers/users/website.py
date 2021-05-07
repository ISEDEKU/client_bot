from aiogram import types

from loader import dp


@dp.message_handler(text='Сайт')
async def website(message: types.Message):
    await message.answer(
        'Ссылки на нашем сайте:\nhttps://aparat.ua/o-magazine'
        '\nhttps://aparat.ua/informaciya-o-dostavke'
        '\nhttps://aparat.ua/kontakty'
        '\nhttps://aparat.ua/ua/faq'
        '\nhttps://aparat.ua/ua/news'
        '\nhttp://apparat.kiev.ua/'
        '\nhttps://aparat.ua/specials/'
        '\nhttps://aparat.ua/podarochnye-sertifikaty/', disable_web_page_preview=True
    )