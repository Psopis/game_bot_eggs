from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from infrastructure.database.db_working import UserWorking
from tgbot.keyboards.inline.main_profile.details_kb import profile_dop_section
from tgbot.keyboards.inline.main_profile.partner.partners_kb import partner_dop_section
from tgbot.keyboards.reply.profile_kb import main_user_profile

from tgbot.keyboards.reply.promo_cancel import cancel_promo

dop_router = Router()


class states(StatesGroup):
    activate_promo = State()


@dop_router.callback_query(F.data == 'activate_promo')
async def textfor_set_promorcode(call: CallbackQuery, state: FSMContext):
    await call.answer()

    text = f"""*Введите промокод:*"""
    await call.message.answer(text=text, parse_mode="Markdown",
                              reply_markup=cancel_promo())
    await state.set_state(states.activate_promo)


@dop_router.message(F.text == '❌Отменть')
async def set_promocode(message: Message, state: FSMContext):
    await message.answer(text=f'Действие отменено', reply_markup=main_user_profile())
    user = await UserWorking.get_user(message.from_user.id)
    text = f"""В нашем боте включена система промокодов. Приглашайте друзей и зарабатывайте на этом!
Чем больше использований Вашего промокода - тем больше вы будете получать!
Статистика:
Ваш промокод: -{user.activated_promo}
Доступно для вывода: 0 ₽
Приведено рефералов: 0
Награда за активацию: -"""
    await message.answer(text=text, parse_mode="Markdown",
                         reply_markup=profile_dop_section())
    await state.clear()


@dop_router.message(states.activate_promo)
async def set_promocode(message: Message, state: FSMContext):
    ###################################
    # есть поле для активации промокода \/\/\/
    # await UserWorking.activate_promo(message.from_user.id, message.text)
    ###################################
    await message.answer(text=f'Промокод {message.text} введен!', reply_markup=main_user_profile())
    user = await UserWorking.get_user(message.from_user.id)
    text = f"""В нашем боте включена система промокодов. Приглашайте друзей и зарабатывайте на этом!
Чем больше использований Вашего промокода - тем больше вы будете получать!

Статистика:

Ваш промокод: -{user.activated_promo}

Доступно для вывода: 0 ₽
Приведено рефералов: 0
Награда за активацию: -"""
    await message.answer(text=text, parse_mode="Markdown",
                         reply_markup=partner_dop_section())
    await state.clear()


@dop_router.callback_query(F.data == 'back_in_profile')
async def back_button(call: CallbackQuery):
    await call.answer()

    user = await UserWorking.get_user(call.from_user.id)
    text = f"""В нашем боте включена система промокодов. Приглашайте друзей и зарабатывайте на этом!
Чем больше использований Вашего промокода - тем больше вы будете получать!

Статистика:

Ваш промокод: -{user.activated_promo}

Доступно для вывода: 0 ₽
Приведено рефералов: 0
Награда за активацию: -"""
    await call.message.edit_text(text=text, parse_mode="Markdown",
                                 reply_markup=partner_dop_section())
