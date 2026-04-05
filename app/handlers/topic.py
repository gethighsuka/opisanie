from aiogram import Router
from aiogram.types import CallbackQuery

from app.states.form import Form

router = Router()

@router.callback_query(Form.choosing_topic)
async def topic_handler(callback: CallbackQuery, state):
    await state.update_data(topic=callback.data)
    await state.set_state(Form.choosing_hashtags)

    await callback.message.answer("Сколько хештегов? (0-6)")
    await callback.answer()