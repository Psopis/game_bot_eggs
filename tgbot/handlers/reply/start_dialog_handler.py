from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import F, types
from aiogram import Router

from infrastructure.neuro.gpt.chat_gpt import gpt_answer
from tgbot.keyboards.reply.profile_kb import main_user_profile

router = Router()
router.message.filter(
    F.chat.type == "private"
)


class Dialog(StatesGroup):
    start_gpt = State()


@router.message(F.text == "📝Начать диалог")
async def with_puree(message: types.Message, state: FSMContext):
    await state.update_data(messages=[])
    text = """Диалог начат!

Чтобы его завершить, нажмите на кнопку "👋🏻 Закончить диалог" или отправьте команду /end.

Приятного общения!"""
    kb = [
        [types.KeyboardButton(text="Закончить диалог")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(text=text, reply_markup=keyboard)
    await state.set_state(Dialog.start_gpt)


@router.message(F.text == "Закончить диалог")
@router.message(Command('end'))
async def with_puree(message: types.Message, state: FSMContext):
    kb = [
        [types.KeyboardButton(text="📝Начать диалог")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Диалог закончен!", reply_markup=main_user_profile())
    await state.clear()


@router.message(Dialog.start_gpt)
async def question_gpt(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    msg = await message.answer(text='Навожу магию, секунду 🪄')
    user_data["messages"].append(
        {
            "role": "user",
            "content": message.text.lower(),
        })
    bot_message = gpt_answer(user_data["messages"])

    await message.bot.edit_message_text(text=bot_message,chat_id=message.chat.id, message_id=msg.message_id)
    user_data["messages"].append(
        {
            "role": "bot",
            "content": bot_message,
        })
    await state.update_data(messages=user_data["messages"])

