from loader import dp
import string

from utils.converter import ogg2wav, wav2text

from aiogram.dispatcher import FSMContext
from aiogram import types
import random



@dp.message_handler(content_types=types.ContentTypes.VOICE, chat_type=types.ChatType.PRIVATE)
async def start_handler(message: types.Message, state: FSMContext):

    await state.finish()

    # this message will be edited
    message_to_edit = await message.reply("✒️ <b>Обработка...</b>")

    file_id = message.voice.file_id
    file = await dp.bot.get_file(file_id)
    file_path = file.file_path

    # random string for filename definition
    rand_string = ''.join(random.choice(string.ascii_letters) for i in range(6))

    # downloading file from telegram
    await dp.bot.download_file(file_path, f"data/storage/{rand_string}.oga")

    # converting file to .wav from .ogg
    file_wav = ogg2wav.Converter().ogg2wav(f"data/storage/{rand_string}.oga", f"data/storage/{rand_string}.wav")

    # recognizing into text
    res_text = wav2text.Recognizer().wav2text(file_wav)

    await message_to_edit.edit_text(f"""
✒️ Обработано:\n
{res_text['transcription']}
""")
    