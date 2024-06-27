from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def profile_subscribes():
    kb = InlineKeyboardBuilder()
    
    kb.row(InlineKeyboardButton(
        text="👤Начальный", callback_data="Start_sub"
    )
    )

    kb.row(InlineKeyboardButton(
        text="⭐Продвинутый", callback_data="Propd_sub"
    )
    )
    kb.row(InlineKeyboardButton(
        text="🔥PRO", callback_data="PRO_sub"
    )
    )
    kb.row(InlineKeyboardButton(
        text="🔙Вернутся в профиль", callback_data="back_in_profile"
    )
    )
    return kb.as_markup()