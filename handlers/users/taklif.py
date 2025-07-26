from aiogram.types import Message
from loader import dp,db,bot
from aiogram import F
from aiogram.fsm.context import FSMContext #new
from states.reklama import OfferState
from data.config import MY_GROUP

@dp.message(F.text == "📩 Murojaat")
async def taklif_yubor(message:Message,state:FSMContext):
    await message.answer("Murojaatingiz matnini kiriting...")
    await state.set_state(OfferState.offer)

@dp.message(OfferState.offer, F.text)
async def qabul(message: Message, state: FSMContext):
    await state.clear()
    text = message.text
    msg = f"📌 Yangi xabar\n"
    msg += f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n\n"
    msg += f"{message.text}"

    # Foydalanuvchining ID sini yuborilayotgan xabarga bog‘lab qo‘yish
    await bot.send_message(
        chat_id=MY_GROUP,
        text=msg,
        parse_mode='HTML'
    )

    await message.answer("📩 Sizning murojaatingiz qabul qilindi. Tez orada javob beramiz.")

@dp.message(F.reply_to_message, F.text)
async def answer_offer(message: Message):
    if message.reply_to_message.text and message.reply_to_message.text.startswith("📩 Admindan xabar:"):
        full_name = message.from_user.full_name
        user_id = message.from_user.id

        msg = f"✉️ *Foydalanuvchidan javob:*\n"
        msg += f"[{full_name}](tg://user?id={user_id})\n\n"
        msg += f"{message.text}"

        await bot.send_message(chat_id=MY_GROUP, text=msg, parse_mode="Markdown")
    else:
        chat_id = message.reply_to_message.entities[0].user.id
        try:
            await bot.send_message(
                chat_id=chat_id,
                text=f"📩 *Admindan xabar:*\n\n{message.text}",
                parse_mode="Markdown"
            )
            await message.answer("✅ Xabaringiz foydalanuvchiga yuborildi.")
        except:
            await message.answer("❌ Xabaringiz foydalanuvchiga yuborilmadi.")



@dp.message(F.text == "💻 Backend")
async def send_backend_course(message: Message):
    photo = "https://i.pinimg.com/736x/12/8e/20/128e2068222c55c941e4342e851d831d.jpg"  # Rasm yo'lini to'g'rilang
    caption = """<b>🖥 Backend Dasturlash (Python) Kursi</b>

1-oy: 🟠 Python Asoslari
Algoritmlash, Python dasturlash asoslari (basic)
600 000 so‘m

2-oy: 🔵 Python Advanced
OOP, Fayllar bilan ishlash, Qiziqarli loyihalar
<i>650 000 so‘m</i>

3-oy: 🟠 Telegram Bot
Aiogram va Telebot asosida 15+ bot yaratish
<i>700 000 so‘m</i>

4-oy: 🔵 Django Web
Web sayt, portfolio, GitHub, Ma’lumotlar bazasi, 5+ Web sayt
<i>750 000 so‘m</i>

🎯 Natija: “Strong Junior” daraja
🎓 Xalqaro darajadagi Sertifikat olish imkoniyati bor"""
    
    await message.answer_photo(photo=photo, caption=caption,parse_mode="html")


@dp.message(F.text == "🇸🇦 Arab tili")
async def send_arab_course(message: Message):
    text = """
<b>🇸🇦 Arab tili kursi (A1 dan B2 gacha)</b>

⸻

<b>🟠 A1 – Arab tili asoslari (3 oy)</b>
🔤 Alifbo, oddiy gaplar, o‘zini tanishtirish, asosiy grammatika, kundalik suhbatlar
💰 <b>330 000 so‘m</b>

⸻

<b>🔵 A2 – Kundalik suhbat va muloqot (3 oy)</b>
📌 O‘tgan zamon, hayotiy vaziyatlar, xat va email yozish, eshitish ko‘nikmalari
💰 <b>330 000 so‘m</b>

⸻

<b>🟠 B1 – Kasb va o‘qish uchun til (3 oy)</b>
🗂 Grammatikani chuqurlashtirish, taqdimot tayyorlash, rezyume va motivatsion xat yozish, og‘zaki nutqni rivojlantirish
💰 <b>380 000 so‘m</b>

⸻

<b>🔵 B2 – Xalqaro darajadagi muloqot (3 oy)</b>
💬 Murakkab grammatik mavzular, yozma va og‘zaki nutq, rasmiy va norasmiy uslubdagi muloqot
💰 <b>380 000 so‘m</b>

⸻

<b>🎓 Imtihonga tayyorgarlik (2 oy)</b>
📝 Model testlar, imtihon simulyatsiyasi, strategiyalar, individual xatolar ustida ishlash
💰 <b>450 000 so‘m</b>

⸻

<b>📌 Davomiyligi:</b> 14 oy
<b>🎯 Natija:</b> Chet elda o‘qish va ishlash uchun kuchli B1 va B2 darajasi
<b>🎓 Sertifikatlar:</b> Goethe, Milliy CEFR va At Tanal

⸻

<b>📚 Darslar kimlar uchun:</b>
👶 7–14 yosh – alohida guruhlar
🧑 14–45 yosh – alohida guruhlar
👴 45–100 yosh – alohida metodika va darsliklar bilan
"""

    await message.answer(text, parse_mode="HTML")
