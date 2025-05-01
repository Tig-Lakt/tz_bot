from aiogram import types
from aiogram.filters.command import Command
from aiogram import Router

from resources import (
    start_text,
    head_menu_kb,
)


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды `/start`.
    """
    await message.answer(
                        text=start_text,
                        reply_markup=head_menu_kb.as_markup(resize_keyboard=True)
                        )
