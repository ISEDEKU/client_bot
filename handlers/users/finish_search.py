from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.main_keyboard import menu_1
from loader import dp


@dp.message_handler(text='Завершить поиск', state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await message.answer('Поиск завершён!', reply_markup=menu_1)
    await state.reset_state()
    await state.finish()