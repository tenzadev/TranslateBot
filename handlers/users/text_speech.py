from aiogram import types
from loader import dp, BASE_DIR
from states.main import TranslateText
from aiogram.dispatcher import FSMContext
from keyboards.default.main import markup
from gtts import gTTS


@dp.callback_query_handler(text="tts", state=TranslateText.speech)
async def gtts_text(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    data = await state.get_data()
    text = data.get("text")
    lang = data.get("lang2")
    await call.answer("Audio saqlandi!", show_alert=True)
    tts = gTTS(text, lang=lang)
    tts.save(f"utils/audios/{call.from_user.id}.mp3")
    await call.message.answer_audio(audio=open(f"{BASE_DIR}/utils/audios/{call.from_user.id}.mp3", "rb"), reply_markup=markup)
    await TranslateText.lang.set()  
