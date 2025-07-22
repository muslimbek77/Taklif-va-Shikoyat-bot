from aiogram.types import Message
from loader import dp,db,bot
from aiogram import F
from aiogram.fsm.context import FSMContext #new
from states.reklama import OfferState
from data.config import MY_GROUP

@dp.message(F.text == "📩 Murojaat")
async def taklif_yubor(message:Message,state:FSMContext):
    await message.answer("Murojaatingiz matnini yuboring...")
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
    try:
        await bot.send_message(chat_id=chat_id,text=message.text)
        await message.answer("Xabaringiz foydalanuvchiga yuborildi...")
    except:
        await message.answer("Xabaringiz foydalanuvchiga yuborilmadi...")



from aiogram.types import FSInputFile

@dp.message(lambda msg: msg.text == "💻 Backend")
async def send_backend_course(message: Message):
    photo = "https://i.pinimg.com/736x/12/8e/20/128e2068222c55c941e4342e851d831d.jpg"  # Rasm yo'lini to'g'rilang
    caption = """🖥 Backend Dasturlash (Python) Kursi

1-oy: 🟠 Python Asoslari
Algoritmlash, Python dasturlash asoslari (basic)
600 000 so‘m

2-oy: 🔵 Python Advanced
OOP, Fayllar bilan ishlash, Qiziqarli loyihalar
650 000 so‘m

3-oy: 🟠 Telegram Bot
Aiogram va Telebot asosida 15+ bot yaratish
750 000 so‘m

4-oy: 🔵 Django Web
Web sayt, portfolio, GitHub, Ma’lumotlar bazasi, 5+ Web sayt
800 000 so‘m

🎯 Natija: “Strong Junior” daraja
🎓 Xalqaro darajadagi Sertifikat olish imkoniyati bor"""
    
    await message.answer_photo(photo=photo, caption=caption)
