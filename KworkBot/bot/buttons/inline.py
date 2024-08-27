from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def make_inline_button(data : list):
    ikb = InlineKeyboardBuilder()
    ikb.add(*[
        InlineKeyboardButton(text =i.name , callback_data=f"{i.id}") for i in data
    ])
    ikb.adjust(2, repeat=True)
    return ikb.as_markup()