from aiogram.types import Message
from loader import dp,db, ADMINS
from aiogram.filters import CommandStart
from keyboard_buttons.taklif_button import taklif_btn
@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz",reply_markup=taklif_btn)
    except:
        await message.answer(text="Assalomu alaykum",reply_markup=taklif_btn)

