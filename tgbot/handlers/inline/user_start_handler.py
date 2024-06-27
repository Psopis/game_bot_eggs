

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from infrastructure.database.db_working import UserWorking
from tgbot.keyboards.inline.subscrbe_check_kb import subscribe_check
from tgbot.keyboards.reply.profile_kb import main_user_profile

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    if await UserWorking.check_user(message.from_user.id):
        await message.answer(
            """Привет! Я - Эдя, бот с искусственным интеллектом. \nТы можешь задать мне любой вопрос, а я на него отвечу☺️""",
            reply_markup=main_user_profile())
    else:
        text = """🔔 Для использования бота подпишитесь на новостной канал, чтобы получать уведомления о новых возможностях и обновлениях бота. Спасибо!
    
    🔔 To use the bot subscribe to the news channel to receive notifications about new features and updates of the bot. Thank you!"""
        await message.answer(text, reply_markup=subscribe_check())
