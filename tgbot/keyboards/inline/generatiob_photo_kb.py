from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def category_neuro():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="🖼️Генерация изображений",
        callback_data="generation_photo"
    )
    )
    kb.row(InlineKeyboardButton(
        text="📷Обработка фото", callback_data="photo_remake"
    )
    )

    kb.row(InlineKeyboardButton(
        text="📼Видео", callback_data="video_remake"
    )
    )
    return kb.as_markup()
