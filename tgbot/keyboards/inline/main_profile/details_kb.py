
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def profile_dop_section():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="⚡Подписка",
        callback_data="_Subscribe"
    )
    )
    kb.row(InlineKeyboardButton(
        text="🤝Партнерская программа", callback_data="_partner_prog"
    )
    )

    kb.row(InlineKeyboardButton(
        text="🫂Поддержка", callback_data="_help"
    )
    )
    return kb.as_markup()
