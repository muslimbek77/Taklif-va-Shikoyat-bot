from aiogram.types import Message
from loader import dp,db,bot
from aiogram import F
from aiogram.fsm.context import FSMContext #new
from states.reklama import OfferState
from keyboard_buttons import taklif_button
from data.config import MY_CHANNEL

@dp.message(F.text == "Taklif va shikoyat")
async def taklif_yubor(message:Message,state:FSMContext):
    await message.answer("Taklifinigiz yoki Shikoyatingiz bo'lsa yuboring...")
    await state.set_state(OfferState.offer)

@dp.message(OfferState.offer)
async def qabul(message:Message,state:FSMContext):
    message_id = message.message_id
    from_chat_id = message.from_user.id
    await bot.copy_message(chat_id=MY_CHANNEL,from_chat_id=from_chat_id,message_id=message_id)
    await message.answer("Sizning murojaatingiz qabul qilindi. Biz uni tez orada ko'rib chiqamiz...")

