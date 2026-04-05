from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.keyboards.inline import topics_keyboard
from app.states.form import Form

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message, state):
    await state.set_state(Form.choosing_topic)
    await message.answer("Выбери игру:", reply_markup=topics_keyboard())