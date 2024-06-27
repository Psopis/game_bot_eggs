
from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from infrastructure.database.db_working import UserWorking
from tgbot.keyboards.inline.main_profile.details_kb import profile_dop_section
from tgbot.keyboards.inline.main_profile.partner.partners_kb import partner_dop_section


dop_router = Router()


class states(StatesGroup):
    generation_photo = State()


@dop_router.callback_query(F.data == '_partner_prog')
async def choosing_neuro_to_txtimg(call: CallbackQuery, state: FSMContext):
    await call.answer()
    user = await UserWorking.get_user(call.from_user.id)
    text = f"""В нашем боте включена система промокодов. Приглашайте друзей и зарабатывайте на этом!
Чем больше использований Вашего промокода - тем больше вы будете получать!

Статистика:

Ваш промокод: -{user.activated_promo}

Доступно для вывода: 0 ₽
Приведено рефералов: 0
Награда за активацию: -"""
    await call.message.answer(text=text,
                              reply_markup=partner_dop_section())


@dop_router.callback_query(F.data == 'back_in_profile')
async def back_button(call: CallbackQuery):
    await call.answer()
    user = await UserWorking.get_user(call.from_user.id)

    text = f"""     👤 *Ваш профиль* `{user.username}`\n
    *Идентификатор:* `{user.user_id}`\n
    📊 Информация:
    *Последний день подписки:* `{user.date}`

                    """
    await call.message.edit_text(text=text, parse_mode="Markdown",
                                 reply_markup=profile_dop_section())
