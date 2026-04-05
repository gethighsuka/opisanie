from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    choosing_topic = State()
    choosing_hashtags = State()