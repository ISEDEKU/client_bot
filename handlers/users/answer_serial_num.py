import os
import urllib

import openpyxl
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.state_class import Questions


@dp.message_handler(state=Questions.serial_num)  # указываю второе состояние
async def answer_serial_num(message: types.Message, state=FSMContext):
    urllib.request.urlretrieve('http://aparat.ua/cli/telegram_opt.xlsx', 'out.xlsx')
    path_to_file = os.path.abspath('out.xlsx')
    book = openpyxl.open(path_to_file, read_only=True)  # открываем книгу, в аргументе указываем путь к файлу
    sheet = book.active  # получаем первый и единственный лист

    data = await state.get_data()
    i = data.get('answer2')
    serial_num = int(i)
    answer = message.text

    if answer.isdigit() == True and int(answer) < i:
        answer = int(message.text)
        sheet_cells = data.get('answer1')
        sel_num = answer
        sel_num = sheet_cells[sel_num - 1]
    else:
        sel_num = []

    # вытаскиваем из хранилища лист, который когда-то сохранили, вот он и пригодился

    if len(sel_num) == 0:
        await message.answer('Такого номера в списке нет...\nВведите номер ещё раз:')
        await Questions.serial_num.set()

    elif len(sel_num) == 2:
        sel_num = int(sel_num[1])
        product_name = sheet[sel_num][1].value
        quantity = sheet[sel_num][3].value
        cost_grn = sheet[sel_num][7].value
        if int(quantity) < 3 or quantity == ' ':
            quantity = 'Уточните у менеджера'
        else:
            quantity = 'Есть в наличии'
        # алгоритм который берёт ячейку из списка, и выдаёт всю нужную информацию в строке с этой ячейкой
        await message.answer(
            '\n{}\nКол-во: {}\nРРЦ $ грн: {}'.format(product_name,
                                                     quantity,
                                                     cost_grn.lstrip()))
        await message.answer(
            'Вы можете посмотреть остальные товары, просто введите другой номер')
        # await state.finish()

    elif len(sel_num) > 2:
        sel_num = sel_num[1:]
        sel_num = int(sel_num)
        product_name = sheet[sel_num][1].value
        quantity = sheet[sel_num][3].value
        cost_grn = sheet[sel_num][7].value
        if int(quantity) < 3 or quantity == ' ':
            quantity = 'Уточните у менеджера'
        else:
            quantity = 'Есть в наличии'
        # алгоритм который берёт ячейку из списка, и выдаёт всю нужную информацию в строке с этой ячейкой
        await message.answer(
            '\n{}\nКол-во: {}\nРРЦ $ грн: {}'.format(product_name,
                                                     quantity,
                                                     cost_grn.lstrip()))
        await message.answer(
            'Вы можете посмотреть остальные товары, просто введите другой номер')
