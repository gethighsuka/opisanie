from aiogram import Router
from aiogram.types import Message

from app.states.form import Form
from app.services.ai import generate_text
from app.services.hashtags import get_hashtags

router = Router()

@router.message(Form.choosing_hashtags)
async def hashtags_handler(message: Message, state):
    if not message.text.isdigit():
        return await message.answer("Введи число от 0 до 6")

    count = int(message.text)

    if count < 0 or count > 6:
        return await message.answer("Только от 0 до 6")

    data = await state.get_data()
    topic = data["topic"]

    await message.answer("⏳ Генерирую...")

    text = generate_text(topic)
    tags = get_hashtags(topic, count)

    result = f"{text}\n\n{' '.join(tags)}"

    await message.answer(result)
    await state.clear()