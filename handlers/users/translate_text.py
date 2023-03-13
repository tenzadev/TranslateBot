from aiogram import types
from loader import dp
from states.main import TranslateText
from aiogram.dispatcher import FSMContext
from googletrans import Translator
from keyboards.inline.main import inline_markup


translator = Translator()


@dp.message_handler(state=TranslateText.translate)
async def translate_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = message.text
    langs = data.get("langs")
    lang1, lang2 = langs.split("-")
    translated = translator.translate(text, src=lang1, dest=lang2)
    await state.update_data({"text": translated.text, "lang2": lang2})
    await message.answer(translated.text, reply_markup=inline_markup)
    await TranslateText.next()
    
