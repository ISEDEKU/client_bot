from aiogram import types

from keyboards.inline.soc_net import soc_net_keyboard
from loader import dp


@dp.message_handler(text='📱 Соцсети')
async def soc_net(message: types.Message):
    await message.answer('Мы в соцсетях', reply_markup=soc_net_keyboard)
    # await message.answer(
    #     'Мы в соцсетях:'
    #     '\nhttps://www.facebook.com/apparatgps'
    #     '\nhttps://www.instagram.com/aparat.ua'
    #     '\nhttps://www.youtube.com/apparatkievua'
    #     '\nhttps://t.me/aparatua', disable_web_page_preview=True
    # )