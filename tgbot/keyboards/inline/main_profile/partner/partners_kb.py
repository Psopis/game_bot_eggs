
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def partner_dop_section():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="💸Вывести Баланс",
        callback_data="get_money"
    )
    )
    kb.row(InlineKeyboardButton(
        text="📍Активировать промокод", callback_data="activate_promo"
    )
    )

    kb.row(InlineKeyboardButton(
        text="⭐Создать промокод", callback_data="create_promo"
    )
    )
    kb.row(InlineKeyboardButton(
        text="🔙Вернутся в профиль", callback_data="back_in_profile"
    )
    )

    return kb.as_markup()
