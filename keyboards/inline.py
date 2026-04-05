from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.data.topics import TOPICS

def topics_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=key)]
            for key, name in TOPICS.items()
        ]
    )