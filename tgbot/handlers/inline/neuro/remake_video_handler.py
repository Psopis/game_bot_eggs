from aiogram import Router, F

from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from tgbot.keyboards.inline.neuro_choose_kb import category_neuro_video

gen_router = Router()


class states(StatesGroup):
    generation_photo = State()


@gen_router.callback_query(F.data == 'video_remake')
async def subscribe_ch(call: CallbackQuery):
    await call.answer()


@gen_router.callback_query(F.data == 'back_neuro')
async def back_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='Выберите нейросеть для генерации:',
                                 reply_markup=category_neuro_video())
