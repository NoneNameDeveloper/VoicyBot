from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram import types

from utils.database.models import User


@dp.message_handler(text="/start", chat_type=['group', 'supergroup'])
async def start_handler(message: types.Message, state: FSMContext):

    await state.finish()

    # group registration step
    exists =  await User.objects.filter(User.user_id == message.chat.id).exists()

    if not exists:
        await User.objects.create(user_id = message.chat.id)
    
    await message.answer("<b>👩‍🎨 Пришли мне голосовое, я переведу его в текст.\nИсходный код: https://github.com/NoneNameDeveloper/VoicyBot</b>")
    