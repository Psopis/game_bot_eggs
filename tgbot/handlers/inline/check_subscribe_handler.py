import datetime

from aiogram import Router, F
from aiogram.types import  CallbackQuery

from infrastructure.database.db_working import UserWorking
from tgbot.config import load_config
from tgbot.keyboards.inline.subscrbe_check_kb import subscribe_check
from tgbot.keyboards.reply.profile_kb import main_user_profile

sub_router = Router()

config = load_config(".env")


@sub_router.callback_query(F.data == 'subscribe_check_')
async def subscribe_ch(call: CallbackQuery):
    await call.answer()

    check = True

    chat_member = await call.bot.get_chat_member(config.tg_bot.chat_id, call.from_user.id)

    if chat_member.status.split('.')[0] == 'left':
        await call.message.answer('Вы не подписались на все каналы!!!', reply_markup=subscribe_check())
        check = False

    if check:
        await call.message.delete()
        print('added', call.from_user.username)
        await UserWorking.add_user(username=call.from_user.username, user_id=call.from_user.id,
                                   time=datetime.date.today() )
        await call.message.answer(
            """Привет! Я - Эдя, бот с искусственным интеллектом. \nТы можешь задать мне любой вопрос, а я на него отвечу☺️""",
            reply_markup=main_user_profile())
