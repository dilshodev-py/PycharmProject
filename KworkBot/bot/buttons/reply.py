from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _



def main_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text=_("🧑🏻‍💻 I am a freelancer")),
        KeyboardButton(text=_("👤 I am a customer")),
        KeyboardButton(text=_("💼 Vacancies/Vacancy placement")),
        KeyboardButton(text=_("Language 🇬🇧🇺🇿🇷🇺"))
    ])
    rkb.adjust(2,1,1)
    return rkb.as_markup(resize_keyboard=True)

def lang_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text = "English 🇬🇧"),
        KeyboardButton(text = "O'zbek 🇺🇿"),
        KeyboardButton(text = "Русский 🇷🇺"),
        KeyboardButton(text = _("⬅️ back"))
    ])
    rkb.adjust(3 , 1)
    return rkb.as_markup(resize_keyboard= True)

def contact_button():
    contact_btn = KeyboardButton(text = _("☎️ Phone Number") , request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[contact_btn]] , resize_keyboard=True)
