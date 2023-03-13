from aiogram.dispatcher.filters.state import StatesGroup, State

class TranslateText(StatesGroup):
    lang = State()
    translate = State()
    speech = State()
