from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _

from bot.buttons.inline import make_inline_button
from bot.buttons.reply import contact_button, main_menu
from bot.state import RegisterEmployeeState
from db.models import Category, Job, User, UserJob

employee_router = Router()


@employee_router.message(F.text == __('🧑🏻‍💻 I am a freelancer'))
async def freelancer_button_handler(message : Message , state : FSMContext):
    await state.set_state(RegisterEmployeeState.contact)
    await message.answer(_("Click the Send Contact button") , reply_markup=contact_button())

@employee_router.message(F.contact,RegisterEmployeeState.contact)
async def contact_handler(message : Message , state : FSMContext):
    await state.update_data({"phone_number" : message.contact.phone_number})
    await state.set_state(RegisterEmployeeState.description)
    await message.answer(_("Briefly about yourself ✍🏻"), reply_markup=ReplyKeyboardRemove())
@employee_router.message(RegisterEmployeeState.description)
async def contact_handler(message : Message , state : FSMContext):
    await state.update_data({"description" : message.text})
    await state.set_state(RegisterEmployeeState.category)
    categories: list[Category] = await Category().objects
    await message.answer(_("Choose your category !") , reply_markup=make_inline_button(categories))


@employee_router.callback_query(RegisterEmployeeState.category)
async def contact_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterEmployeeState.job)
    jobs = await Job(category_id = callback.data).filter_by_category()
    await callback.message.edit_text(_("Choose your job !"), reply_markup=make_inline_button(jobs))


@employee_router.callback_query(RegisterEmployeeState.job)
async def contact_handler(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await User(id=callback.from_user.id).update(phone_number=data.get("phone_number"), description = data.get("description"))
    await UserJob(user_id = callback.from_user.id , job_id= callback.data).save()
    await state.clear()
    await callback.message.delete()
    await state.update_data({"locale" : data.get("locale")})
    await callback.message.answer(_("Success"), reply_markup=main_menu())





