from aiogram import types
from loader import dp
from states.main import TranslateText
from aiogram.dispatcher import FSMContext

lang_code = {
    "🇺🇿 Uzb - 🇬🇧 Eng": "uz-en",
    "🇬🇧 Eng - 🇺🇿 Uzb": "en-uz",
    "🇺🇿 Uzb - 🇷🇺 Rus": "uz-ru",
    "🇷🇺 Rus - 🇺🇿 Uzb": "ru-uz"
}


@dp.message_handler(lambda message: message.text in lang_code.keys(), state=TranslateText.lang)
async def get_lang(message: types.Message, state: FSMContext):
    lang = message.text
    await state.update_data({"langs": lang_code.get(lang)})
    await message.answer("Tarjima qilmoqchi bo'lgan matningizni yuboring!")
    await TranslateText.next()