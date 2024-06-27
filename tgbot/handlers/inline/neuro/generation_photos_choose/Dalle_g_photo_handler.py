
import shutil
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery,  FSInputFile

from infrastructure.neuro.Dalle.get_dalle import get__dalle
from tgbot.keyboards.inline.generatiob_photo_kb import category_neuro
from tgbot.keyboards.reply.profile_kb import main_user_profile

gen_router = Router()


class states(StatesGroup):
    generation_photo = State()


@gen_router.callback_query(F.data == 'D_neuro')
async def send_textimg(call: CallbackQuery, state: FSMContext):
    await call.answer()

    await call.message.answer(text='Напишите описание изображения:', reply_markup=None)
    await state.set_state(states.generation_photo)


@gen_router.message(states.generation_photo)
async def send_text_to_img_neuro(message: Message, state: FSMContext):
    await message.answer(text='Навожу магию, секунду 🪄')
    photo = get__dalle(message.text)

    await message.bot.send_photo(chat_id=message.chat.id, photo=FSInputFile(photo))
    await message.answer(text="Фотография получена!", reply_markup=main_user_profile())
    shutil.rmtree(photo[:-11])
    await state.clear()


@gen_router.callback_query(F.data == 'back_neuro')
async def back_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='Выберите нейросеть для генерации:',
                                 reply_markup=category_neuro())
