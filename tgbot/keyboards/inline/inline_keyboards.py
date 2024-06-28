from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.web_app import WebAppInitData, WebAppUser, WebAppChat
from aiogram.types.web_app_info import WebAppInfo

class Profile_kb:
    @staticmethod
    def start_keyboard():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Играть",
            callback_data=f'start_game'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Рейтинг",
            callback_data=f'get_rating'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Указать ID",
            callback_data=f'set_ID'
        )
        )
        return kb.as_markup()

    @staticmethod
    def set_id_keyboard():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Указать новый ID",
            callback_data=f'set_new_ID'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Вернутся назад",
            callback_data=f'get_back_from_ID'
        )
        )
        return kb.as_markup()

    @staticmethod
    def start_game_and_play():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Играть",
            web_app=WebAppInfo(url="https://psopis.github.io/site_game_create/")
        )
        )
        kb.row(InlineKeyboardButton(
            text="Вернутся назад",
            callback_data=f'get_back_from_ID'
        )
        )
        return kb.as_markup()



