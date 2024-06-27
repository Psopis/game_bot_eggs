from aiogram.types import Message
from aiogram import F
from aiogram import Router

from tgbot.keyboards.inline.generatiob_photo_kb import category_neuro

router = Router()
router.message.filter(
    F.chat.type == "private"
)


@router.message(F.text == "🧠Нейросети")
async def neuro_start_hand(message: Message):
    await message.answer("Выберите категорию генерации:", reply_markup=category_neuro())
