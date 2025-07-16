from aiogram.types import Message
from loader import dp,db,bot
from aiogram import F
from aiogram.fsm.context import FSMContext #new
from states.reklama import OfferState
from data.config import MY_GROUP

@dp.message(F.text == "Taklif va shikoyat")
async def taklif_yubor(message:Message,state:FSMContext):
    await message.answer("Taklifinigiz yoki Shikoyatingiz bo'lsa yuboring...")
    await state.set_state(OfferState.offer)

@dp.message(OfferState.offer, F.text)
async def qabul(message:Message,state:FSMContext):
    text = message.text
    msg = f"📌 Yangi xabar\n"
    msg += f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n\n"
    msg += f"{message.text}"
    await bot.send_message(chat_id=MY_GROUP,text=msg,parse_mode='html')

    await message.answer("Sizning murojaatingiz qabul qilindi. Biz uni tez orada ko'rib chiqamiz...")

@dp.message(F.reply_to_message, F.text)
async def answer_offer(message:Message):
    
    chat_id = message.reply_to_message.entities[0].user.id

    await bot.send_message(chat_id=chat_id,text=message.text)