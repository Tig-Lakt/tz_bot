import re
from aiogram import types
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from database.database import (  
    insert_data,
    del_data,
)

from resources import (
    head_menu_kb,
)

from functions import read_file, get_average_price
from resources import add_file_text
from config import TOKEN, USER_FILE
from states import UserData


router = Router()
bot = Bot(token=TOKEN)


@router.callback_query(F.data == 'add_file')
async def f_add_file(callback: types.CallbackQuery, state: FSMContext):
    """
    Обработчик callback-запроса с data "add_file".

    Удаляет предыдущее сообщение и предлагает пользователю отправит файл.
    """
    await callback.message.delete()
    await callback.message.answer(
                                  add_file_text
    )

    await state.set_state(UserData.waiting_file)


@router.message(UserData.waiting_file, F.document)
async def f_save_file(message: types.Message, state: FSMContext):
    """
    Состояние ожидание отправки файла пользователем.

    Сохранение файла.

    Отправка пользователю содержимого файла в виде текста.

    Обработка файла вспомогательными функциями, отправка пользователю 
    вычисленного среднего значения
    """
    await bot.download(message.document, destination=USER_FILE)
    result_data = await read_file()

    res_list = ''
    for index, row in result_data.iterrows():
        res_list = res_list + row['title'] + ' ' + row['url'] + ' ' + row['xpath'] + ' ' + str(row['price']) + '\n'
        
    await message.answer(res_list)

    for index, row in result_data.iterrows():
        price = row['price']
        if type(price) != int:
            price = re.sub('\D', '', price) # Очистка значения цены от лишних симолов
        await insert_data(row['title'], row['url'], row['xpath'], price) # Загрузка данных в БД

    msg = await get_average_price() # Полуение средней цены для каждого сайта
    await message.answer(
                        msg,
                        reply_markup=head_menu_kb.as_markup(resize_keyboard=True)
                        )

    await del_data() # Очистка таблицы links