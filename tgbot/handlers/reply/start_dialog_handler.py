from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import F, types
from aiogram import Router

router = Router()
router.message.filter(
    F.chat.type == "private"
)


class Dialog(StatesGroup):
    start_gpt = State()



