from aiogram.types import Message
from loader import dp
from aiogram import F
from keyboard_buttons.taklif_button import social_keyboard

@dp.message(F.text == "🌐 Ijtimoiy tarmoqlarda biz")
async def send_social_links(message: Message):
    await message.answer(
        "🌐 Ijtimoiy tarmoqlarda bizni kuzatib boring:",
        reply_markup=social_keyboard
    )