from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from infrastructure.database.db_working import UserWorking
from tgbot.keyboards.inline.inline_keyboards import Profile_kb
from tgbot import texts_config
from tgbot.texts_config import TEXTS

user_router = Router()


class states(StatesGroup):
    set_id = State()
    set_name = State()
    set_ID = State()


class User:
    @staticmethod
    @user_router.message(CommandStart())
    async def user_start(message: Message):

        # if await UserWorking.check_user(message.from_user.id):
        #     pass
        text = TEXTS['start_text']
        await UserWorking.add_user(user_id=message.from_user.id, name=message.from_user.username)
        await message.answer(text, reply_markup=Profile_kb.start_keyboard())

    @staticmethod
    @user_router.callback_query(F.data == 'get_rating')
    async def get_rating(call: CallbackQuery):
        await call.answer()
        user = await UserWorking.get_user(call.from_user.id)
        text = TEXTS['get_rating']
        await call.message.answer(text)

    @staticmethod
    @user_router.callback_query(F.data == 'set_ID')
    async def get_rating(call: CallbackQuery, state: FSMContext):
        await call.answer()
        user = await UserWorking.get_user(call.from_user.id)
        if user.game_user_id:
            text = TEXTS['set_id_or_set_new_id']
            await call.message.answer(text, reply_markup=Profile_kb.set_id_keyboard())
        else:

            text = TEXTS['set_id_for_prize']
            await call.message.answer(text)
            await state.set_state(states.set_id)

    @staticmethod
    @user_router.callback_query(F.data == 'get_back_from_ID')
    async def get_back(call: CallbackQuery):
        await call.answer()
        text = TEXTS['start_text']
        await call.message.answer(text, reply_markup=Profile_kb.start_keyboard())


class StartGame:
    @staticmethod
    @user_router.callback_query(F.data == 'start_game')
    async def get_rating(call: CallbackQuery, state: FSMContext):
        user = await UserWorking.get_user(call.from_user.id)
        text = TEXTS['start_game']
        await call.message.edit_text(text)
        if user.game_user_id and user.game_name:
            print(1)
            await call.message.edit_text(text=TEXTS['Текст для запуска игры после заполнения имени и id'])
        else:
            print(3)

            await state.set_state(states.set_name)
            text = TEXTS['Текст для ввода имени при запуске игры']
            await call.message.answer(text)

    @staticmethod
    @user_router.message(states.set_name)
    async def user_set_name_(message: Message, state: FSMContext):

        if await UserWorking.check_game_name(message.text):

            text = 'Такое имя уже есть'
            await message.answer(text)
            await state.set_state(states.set_name)
        else:

            await UserWorking.set_game_name(user_id=message.from_user.id, name=message.text)
            await state.clear()

            await message.answer(TEXTS['Текст для ввода ID при запуске игры'])
            await state.set_state(states.set_ID)

    @staticmethod
    @user_router.message(states.set_ID)
    async def user_set__id(message: Message, state: FSMContext):
        print(1221)
        try:
            int(message.text)

        except ValueError:
            await message.answer('инт надо')
        else:
            if await UserWorking.check_game_id(int(message.text)):
                text = 'Такой id уже есть!'
                await message.answer(text)
                await state.set_state(states.set_ID)
                await message.answer(TEXTS['Текст для ввода ID при запуске игры'])
            else:
                await UserWorking.set_game_id(user_id=message.from_user.id, id=int(message.text))
                await message.answer(TEXTS['После ввода имени и id и запуск игры'],
                                     reply_markup=Profile_kb.start_game_and_play())
                await state.clear()
