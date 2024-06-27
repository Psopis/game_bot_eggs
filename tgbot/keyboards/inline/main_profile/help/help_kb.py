from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def helps_kb():
    kb = InlineKeyboardBuilder()

    kb.row(InlineKeyboardButton(
        text="📚База знаний", callback_data="Base_knowleges",url='https://example.com'
    )
    )

    kb.row(InlineKeyboardButton(
        text="👨‍💻Контакт поддержки", callback_data="Contact_hepling",
        url='https://example.com'
    )
    )

    kb.row(InlineKeyboardButton(
        text="🔙Вернутся в профиль", callback_data="back_in_profile"
    )
    )
    return kb.as_markup()
