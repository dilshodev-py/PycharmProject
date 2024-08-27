from aiogram.fsm.state import StatesGroup, State


class ButtonsState(StatesGroup):
    lang = State()


class RegisterEmployeeState(StatesGroup):
    contact = State()
    description = State()
    category = State()
    job = State()

