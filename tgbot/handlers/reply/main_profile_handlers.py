from aiogram.types import Message
from aiogram import F
from aiogram import Router

from infrastructure.database.db_working import UserWorking
from tgbot.keyboards.inline.main_profile.details_kb import profile_dop_section

router = Router()
router.message.filter(
    F.chat.type == "private"
)


@router.message(F.text == "🏡Профиль")
async def main_profile_text(message: Message):
    print(message.from_user.id)
    user = await UserWorking.get_user(message.from_user.id)

    text = f"""     👤 *Ваш профиль* `{user.username}`\n
*Идентификатор:* `{user.user_id}`\n
📊 Информация:
*Последний день подписки:* `{user.date}`

                """
    await message.answer(text=text, parse_mode="Markdown", reply_markup=profile_dop_section())
