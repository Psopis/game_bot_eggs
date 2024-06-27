

from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import  CallbackQuery


from tgbot.keyboards.inline.generatiob_photo_kb import category_neuro
from tgbot.keyboards.inline.neuro_choose_kb import  category_neuro_remake_photo


gen_router = Router()


class states(StatesGroup):
    remake_photo = State()


@gen_router.callback_query(F.data == 'photo_remake')
async def remake_photo_neuro(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='Выберите нейросеть для генерации:',
                                 reply_markup=category_neuro_remake_photo())


@gen_router.callback_query(F.data == '')
async def send_textimg(call: CallbackQuery, state: FSMContext):
    await call.answer()

    # await call.message.answer(text='Напишите описание изображения:', reply_markup=None)
    await state.set_state(states.remake_photo)


@gen_router.callback_query(F.data == 'back_neuro')
async def back_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='Выберите нейросеть для генерации:',
                                 reply_markup=category_neuro())
