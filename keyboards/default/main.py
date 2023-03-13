from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 Uzb - 🇬🇧 Eng"), KeyboardButton(text="🇬🇧 Eng - 🇺🇿 Uzb")],
        [KeyboardButton(text="🇺🇿 Uzb - 🇷🇺 Rus"), KeyboardButton(text="🇷🇺 Rus - 🇺🇿 Uzb")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
