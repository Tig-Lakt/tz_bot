from aiogram.fsm.state import StatesGroup, State


class UserData(StatesGroup):
    """
    FSM для обработки ввода регистрационных данных пользователя.

    Состояния:
        waiting_file (State): Ожидание отправки файла пользователем.
    """
    
    waiting_file = State()