from aiogram.types import Message
from loader import dp
from aiogram import F

@dp.message(F.text=="📍 Bizning Manzil")
async def send_location(message:Message):
    lat = 40.761591
    long = 72.350755
    await message.answer_location(latitude=lat,longitude=long)