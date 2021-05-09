from aiogram import types
from aiogram.utils.markdown import hlink

from loader import dp


@dp.message_handler(text='🔬 Отзывы')
async def reviews(message: types.Message):
    await message.answer(hlink('Відгуки Google',
                               'https://www.google.com/search?q=%EE%F2%E7%FB%E2%FB+aparat.ua&sxsrf=ALeKk00oYaqBfhw3L8C50XF0ml2ZiUy_DA:1617353061189&ei=ZdlmYMj2Cs39rgTNl7yADQ&oq=%EE%F2%E7%FB%E2%FB+aparat.ua&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBggAEAgQHjoHCCMQsAMQJ1D7iwFY948BYNuTAWgBcAB4AIABqgGIAcMCkgEDMi4xmAEAoAEBqgEHZ3dzLXdpesgBAcABAQ&sclient=gws-wiz&ved=0ahUKEwiIvcDVld_vAhXNvosKHc0LD9AQ4dUDCA0&uact=5'),
                         disable_web_page_preview=True)
