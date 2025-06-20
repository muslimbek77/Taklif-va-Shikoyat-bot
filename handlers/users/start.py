from aiogram.types import Message
from filters.admin import IsBotAdminFilter
from loader import dp,db, ADMINS
from aiogram.filters import CommandStart,Command
from keyboard_buttons import admin_keyboard,taklif_button



@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def starts_command(message:Message):
    await message.answer(text="Assalomu alaykum",reply_markup=admin_keyboard.admin_button)

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
    except:
        pass
    await message.answer(text="Assalomu alaykum, bu Renessans Akademiyasinig taklif va shikoyatlar boti...",reply_markup=taklif_button.taklif_btn)
