from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# - клавиатура для добавления файла
btn_add_file = InlineKeyboardButton(text='Добавить файл', callback_data='add_file')

head_menu_wo_subs_btns = [
    btn_add_file,
]

head_menu_kb = InlineKeyboardBuilder()
head_menu_kb.add(*head_menu_wo_subs_btns)
head_menu_kb.adjust(2)