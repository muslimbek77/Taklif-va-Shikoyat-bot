from aiogram.types import Message
from loader import dp
from aiogram import F
from keyboard_buttons.taklif_button import our_course_btn

@dp.message(F.text == "📚 Bizning kurslar")
async def our_courses_func(message:Message):
    await message.answer("Bizning kurslarimiz",reply_markup=our_course_btn)
    