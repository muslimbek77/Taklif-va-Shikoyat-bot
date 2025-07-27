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
    caption = (
    "🖥 <b>Backend Dasturlash (Python) Kursi</b>\n\n"
    "1-oy: 🟠 <b>Python Asoslari</b>\n"
    "Algoritmlash, Python dasturlash asoslari (basic)\n"
    "<b>💰 600 000 so‘m</b>\n\n"
    "2-oy: 🔵 <b>Python Advanced</b>\n"
    "OOP, Fayllar bilan ishlash, Qiziqarli loyihalar\n"
    "<b>💰 650 000 so‘m</b>\n\n"
    "3-oy: 🟠 <b>Telegram Bot</b>\n"
    "Aiogram va Telebot asosida 15+ bot yaratish\n"
    "<b>💰 700 000 so‘m</b>\n\n"
    "4-oy: 🔵 <b>Django Web</b>\n"
    "Web sayt, portfolio, GitHub, Ma’lumotlar bazasi, 5+ Web sayt\n"
    "<b>💰 750 000 so‘m</b>\n\n"
    "🎯 <b>Natija:</b> “Strong Junior” daraja\n"
    "🎓 <i>Xalqaro darajadagi Sertifikat olish imkoniyati bor</i>\n\n"
    "🚀<b>Qo‘shimcha:</b> 2 oy amaliyot, bozor talabidagi dasturlar yaratish,\n"
    "portfolio, CV tayyorlash va ishga joylashishda ko‘mak"
)

    
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


@dp.message(F.text == "📚 Matematika")
async def math_course(message: Message):
    photo = "https://i.ibb.co/Q3hB0YsT/image.png"
    caption = """<b>📚 Kurslar Dasturi (Oyma-oy reja)</b>

⸻

<b>🔹 1. Matematika Standarti</b>  
💰 <b>Har oy: 300 000 so‘m</b>

<b>1-oy:</b> Boshlang‘ich baza  
📘 Usmonov kitobi asosida  
📐 Asosiy formulalar  
🧮 Oddiy misollar bilan tushuncha

<b>2-oy:</b> Asosiy tamoyillar  
📏 Algebraning muhim qoidalari  
✍️ Amaliy mashg‘ulotlar va yechim usullari

<b>Qolgan oylarda:</b> Katta mavzular  
📚 Samarkand va Usmonov kitoblaridan chuqur mavzular  
📝 Har bir mavzu bo‘yicha testlar va misollar  
🧠 Mantiqiy fikrlash va strategiyalar

⸻

<b>🔹 2. SAT Matematika</b>  
💰 <b>Har oy: 400 000 so‘m</b>

<b>1-oy:</b> Kirish va tayyorgarlik  
📊 SAT haqida umumiy tushuncha  
📐 Boshlang‘ich matematik mavzular  
📄 Format bilan tanishish

<b>2-oy:</b> Asosiy mavzular  
➕ Algebra, funktsiyalar, foiz, nisbiylik  
📈 Grafiklar, tenglamalar, so‘rovlar  
🧪 Har bir mavzudan keyin testlar

<b>3-oy:</b> Amaliy mashg‘ulotlar  
🧩 Mock testlar (real imtihon formatida)  
🔍 Xatolarni tahlil qilish  
⏱ Vaqtni boshqarish strategiyalari

<b>Har oyda:</b>  
🖥 Interaktiv darslar  
❓ Savol-javoblar
"""
    await message.answer_photo(photo=photo, caption=caption,parse_mode="html")


@dp.message(F.text == "🇬🇧 Ingliz tili")
async def english_course(message:Message):
    text = """<b>🇬🇧 Ingliz tili kursi (A1 dan B2 gacha)</b>  
🌍 Dunyo bilan bemalol muloqot qiling!

⸻

<b>🟠 A1 – Ingliz tilining asoslari (3 oy)</b>  
🔤 Alifbo, salomlashuv, o‘zini tanishtirish, asosiy grammatik qoidalar, kundalik iboralar  
💬 Oddiy va tushunarli darslar bilan 0 dan boshlang!  
💰 <b>300 000 so‘m</b>

⸻

<b>🔵 A2 – Kundalik muloqot va suhbatlar (3 oy)</b>  
📌 Hayotiy vaziyatlar, yo‘l so‘rash, telefon orqali suhbat, xat va email yozish, eshitib tushunish ko‘nikmalari  
💬 Har kuni kerak bo‘ladigan ingliz tili  
💰 <b>350 000 so‘m</b>

⸻

<b>🟠 B1 – Ish va ta’lim uchun ingliz tili (3 oy)</b>  
🗂 Kengaytirilgan grammatika, taqdimotlar tayyorlash, rezyume, motivatsion xatlar, ish suhbati ssenariylari  
💼 Ish va grantlar uchun mustahkam tayyorgarlik  
💰 <b>400 000 so‘m</b>

⸻

<b>🔵 B2 – Akademik va professional muloqot (3 oy)</b>  
💬 Rasmiy va norasmiy uslublar, murakkab matnlar, akademik ifodalar, og‘zaki va yozma fikrni chuqur bayon qilish  
📚 Universitetga tayyorgarlik yoki xorijiy ish intervyulari uchun kuchli asos!  
💰 <b>500 000 so‘m</b>

⸻

<b>🎓 Imtihonga tayyorgarlik – IELTS, TOEFL, CEFR, Duolingo (2 oy)</b>  
📝 Model testlar, imtihon strategiyalari, speaking & writing bo‘yicha tahlil, individual kamchiliklar bilan ishlash  
📌 IELTS, TOEFL, Duolingo kabi xalqaro sertifikatlarni olish imkoniyati  
💰 <b>550 000 so‘m</b>

⸻

<b>📌 Umumiy davomiylik:</b> 14 oy  
<b>🎯 Natija:</b> Ish, o‘qish va chet elda yashash uchun kerakli darajada – <b>B2</b>!  
<b>🎓 Sertifikatlar:</b> IELTS, TOEFL, CEFR, Duolingo – xalqaro tan olingan hujjatlar!

⸻

<b>✨ Nega aynan ingliz tili?</b>  
🔹 Dunyodagi 1 milliarddan ortiq inson ingliz tilida so‘zlashadi  
🔹 Har bir 4-ta ish e’londan 3 tasi ingliz tilini bilishni talab qiladi  
🔹 Grantlar, vizalar, oliy ta’lim va online kurslarning 90% ingliz tilida  
🔹 Bu til sizga yangi eshiklar ochadi — do‘stlar, karera, sayohat va bilim!

📢 <b>Ingliz tilini o‘rganish — bu investitsiya, hech qachon yo‘qotmaydigan boylik!</b>
"""
    await message.answer(text=text,parse_mode="HTML")


@dp.message(F.text == "🇩🇪 Nemis tili")
async def german_course(message:Message):
    text = """<b>🇩🇪 Nemis tili kursi (A1 dan B2 gacha)</b>

⸻

<b>🟠 3 oy – A1: Nemis tilining asoslari</b>\n
🔤 <i>Alifbo, oddiy gaplar, o‘zini tanishtirish, asosiy grammatik qoidalar, kundalik suhbatlar</i>\n
💰 <b>400 000 so‘m</b>

⸻

<b>🔵 3 oy – A2: Kundalik suhbat va muloqot</b>\n
📌 <i>O‘tgan zamonlar, hayotiy vaziyatlar, xat va email yozish, eshitib tushunish ko‘nikmalari</i>\n
💰 <b>500 000 so‘m</b>

⸻

<b>🟠 3 oy – B1: Kasb va o‘qish uchun til</b>\n
🗂 <i>Grammatikani chuqurlashtirish, taqdimotlar tayyorlash, rezyume va motivatsion xat yozish, og‘zaki nutqni rivojlantirish</i>\n
💰 <b>600 000 so‘m</b>

⸻

<b>🔵 3 oy – B2: Xalqaro darajadagi muloqot</b>\n
💬 <i>Yozma va og‘zaki nutqni kengaytirish, murakkab grammatik mavzular, rasmiy va norasmiy uslublarda muloqot</i>\n
💰 <b>700 000 so‘m</b>

⸻

<b>🎓 2 oy – Imtihonga tayyorgarlik (Goethe, ÖSD, Telc, Milliy, ecl)</b>\n
📝 <i>Model testlar, imtihon simulyatsiyasi, strategiyalar, individual xatolar ustida ishlash</i>\n
💰 <b>800 000 so‘m</b>

⸻

📌 <b>Davomiylik:</b> 14 oy\n
🎯 <b>Natija:</b> Chet elda ishlash va o‘qish uchun zarur kuchli B1 va B2 daraja\n\n
🎓 <i>Goethe, Milliy, Telc, ecl yoki ÖSD xalqaro sertifikat olish imkoniyati mavjud!</i>
"""
    await message.answer(text=text, parse_mode="HTML")


@dp.message(F.text == "🖌️ Grafik Dizayner")
async def graphic_designer(message:Message):
    photo = "https://artcraft.media/img/article/824x464/d92c1e61cd380fca490b7dc72f795b42.jpg"

    caption = """🎨 <b>Grafik Dizayn Kursi (6 oy)</b>

<b>🟢 1-bosqich (2 oy) — Adobe Photoshop</b>
• Photoshop interfeysi bilan ishlash
• Rasm ranglari, kontrast va balansni sozlash
• Foto montaj va kompozitsiya yaratish
• Social media postlar dizayni
• Vizitka va flayer tayyorlash
• Tipografiya asoslari
💰 580 000 so‘mdan

<b>🟢 2-bosqich (2 oy) — Adobe Illustrator</b>
• Illustrator interfeysi bilan ishlash
• Vektor vs raster tushunchalari
• Icon dizayni
• Reklama banner dizayni
• Poligrafiya
• Qadoq dizayni
💰 680 000 so‘mdan

<b>🟢 3-bosqich (2 oy) — Logo va Branding</b>
• Logo sketching (qalamda eskizlar)
• Wordmark, lettermark, abstract logo yaratish
• Ranglar psixologiyasi (color psychology)
• Branding mockup tayyorlash
• Brandbook yaratish
• Mijoz bilan ishlash va brief olish
💰 880 000 so‘mdan
"""

    await message.answer_photo(photo=photo,caption=caption,parse_mode="HTML")


@dp.message(F.text == "🎨 Frontend")
async def frontend_course(message:Message):
    photo = "https://wallpapercave.com/wp/wp9641838.jpg"

    caption = """🎓 <b>Full Frontend va WordPress Kursi (6 oy)</b>

🧩 <b>1-bosqich (1 oy) — WordPress (No Coding)</b>
Hosting va domen bilan ishlash
Yangilik sayti (kun.uz kabi) yaratish
Landing page tayyorlash
2 ta amaliy loyiha
💰 <b>Narxi:</b> 650 000 so‘mdan

💻 <b>2-bosqich (2–2.5 oy) — HTML, CSS, JavaScript</b>
Strukturali sahifa yaratish
Dizayn va interfeyslar
JavaScript asoslari
2 ta amaliy loyiha
💰 <b>Narxi:</b> 700 000 so‘mdan

⚛️ <b>3-bosqich (3–3.5 oy) — React JS, Tailwind CSS, Supabase</b>
Murakkab frontend ilovalar
Internet magazin loyihasi
Supabase bilan backend ulash
Professional web saytlar yaratish
💰 <b>Narxi:</b> 700 000 so‘mdan

🚀 <b>Yakuni (1 oy) — Amaliyot</b>
Real mijozlar bilan ishlash
Portfolio yig‘ish
"""

    await message.answer_photo(photo=photo,caption=caption,parse_mode="HTML")



@dp.message(F.text == "🎭 Shaxsiy Brend (Face brand)")
async def face_brand_course(message:Message):
    text = """🎭 Shaxsiy Brend (Face brand) Kursi
📍 Renessans Academy tomonidan tashkil etilgan amaliy va chuqurlashtirilgan kurs
💸 Kurs narxi (to‘liq 5 oy): 1 500 000 so‘m
🗓 Darslar haftasiga 6 kun davom etadi — intensiv, natijaga yo‘naltirilgan yondashuv
🎓 Kurs yakunida Renessans Academy tomonidan maxsus sertifikat taqdim etiladi

⸻

📌 Kurs haqida umumiy ma’lumot:

“Face brand” kursi — bu sizning nutq, aktyorlik va kontent yaratuvchanligingizni rivojlantirish orqali kuchli shaxsiy brendga aylanish imkonini beruvchi dastur. Kurs sahna va kamera oldida ishonchli chiqish, ijtimoiy tarmoqlarda sifatli kontent yaratish hamda o‘z uslubingizni topishga yo‘naltirilgan.

📚 Kurs muallifi:
Oliy ma’lumotli aktyor, 7 yillik aktyorlik va nutq texnikasi bo‘yicha tajriba, 4 yillik Face Brend yo‘nalishida faol amaliyotga ega.

⸻

🟠 1-oy: Nutq texnikasi va sahnadagi ishonch
 • To‘g‘ri nafas, diksiyaning rivoji, talaffuz
 • Emotsional ifoda, ishonchli chiqishlar
 • Ichki tayyorgarlik va sahnadagi tabiiylik

Bu bosqichda kamera bilan ishlash kiritilmaydi – asosiy e’tibor nutq va sahnadagi erkinlikka qaratiladi.

⸻

🔵 2-oy: Kamera bilan ishlash va aktyorlik mahorati
 • Kamera oldida o‘zini tutish, ifoda, pozitsiya
 • Monolog, she’r, sahnaviy parcha ijrosi
 • Improvizatsiya, his-tuyg‘uni boshqarish va uzatish

⸻

🟠 3-oy: Ssenariy yozish va sun’iy intellekt bilan ishlash
 • G‘oya yaratish, voqeani ssenariyga aylantirish
 • ChatGPT kabi vositalar bilan ishlash: ma’lumot yig‘ish va tahlil
 • Ssenariy strukturasini tuzish va uni ijroga tayyorlash

⸻

🔵 4–5-oy: Amaliyot va Portfolio
 • Kamera oldida real chiqishlar, kontentlar tayyorlash
 • Portfolio yaratish: aktyorlik chiqishlari, ijodiy loyihalar
 • TikTok, Instagram va YouTube formatidagi ijodiy ishlar

⸻

🎁 Qo‘shimcha imkoniyatlar:

🔹 Kurs davomida o‘zini ijobiy va kreativ tarzda ko‘rsatgan o‘quvchilarga Renessans Agency bilan hamkorlik asosida ishlash taklif qilinadi.
🔹 Bu orqali o‘quvchi amaliy tajriba orttiradi va doimiy ijodiy loyihalarda ishtirok etish imkoniyatiga ega bo‘ladi.

⸻

🎯 Natija:
Ishtirokchi sahna va kamera qarshisida ishonchli, kreativ va professional tarzda o‘zini namoyon qila oladigan Face Brend egasiga aylanadi.

🎓 Kurs yakunida Renessans Academy tomonidan rasmiy sertifikat taqdim etiladi, bu sizning malakangizni tasdiqlaydi va portfoliongizda kuchli asos bo‘ladi."""
    await message.answer(text=text)

@dp.message(F.text == "🎯 Target (Reklama Sozlash)")
async def target_course(message:Message):
    text = """Target (Reklama Sozlash) 1 oylik Amaliy Kurs
📍 Renessans Academy tomonidan tashkil etilgan amaliy o‘quv dasturi
💸 Narxi: 1 500 000 so‘m (to‘liq 1 oy)
🗓 Darslar haftasiga 6 kun — intensiv va natijaga yo‘naltirilgan yondashuv
🎓 Kurs yakunida rasmiy sertifikat taqdim etiladi

⸻

📌 Kurs haqida qisqacha:

Ushbu 1 oylik “Target” kursi — sizni 0 dan boshlab, Facebook va Instagram reklamalarini mustaqil tarzda professional sozlash darajasiga olib chiqadi. Kurs davomida siz real kampaniyalar ustida ishlaysiz, mijoz topish, kontent va strategiyani qanday tanlashni o‘rganasiz.

📚 Kurs muallifi:
4 yillik tajribaga ega targetolog, 15+ ta yirik (gigant) loyihalarni muvaffaqiyatli yakunlagan. Real natijalar, strategik yondashuv va amaliy bilimlar asosida dars beradi.

⸻

🔹 Nimalarni o‘rganasiz?

• Facebook Ads Manager bilan ishlash
• Pixel o‘rnatish va konversiyani kuzatish
• Ideal auditoriyani aniqlash va sozlash
• Kreativ reklamalar va A/B testing
• Reklama byudjetini to‘g‘ri taqsimlash
• Natijalarni tahlil qilish va optimallashtirish

⸻

🎁 Bonus:
• Portfolio uchun real reklama kampaniyasi
• Faol ishtirokchilarga Renessans Agency orqali ish takliflari

⸻

🎯 Natija:
1 oy ichida siz mustaqil ishlay oladigan, haqiqiy mijozlar bilan ishlashga tayyor junior targetologga aylanasiz.

🎓 Rasmiy sertifikat sizning bilim va ko‘nikmalaringizni tasdiqlaydi."""
    await message.answer(text=text)


@dp.message(F.text == "🇷🇺 Rus tili")
async def rus_tili(message:Message):
    text = """🇷🇺 Rus tili kursi (1a dan 3b gacha)
⸻

🟠 3 oy – 1a, 1b: Rus tili asoslari

🔤 Alifbo, oddiy gaplar, o‘zini tanishtirish, asosiy grammatik qoidalar, kundalik muloqotlar
💰 Haftada 3 kun — 360000 so‘m
Har kunlik — 620 000 so‘m

⸻

🔵 3 oy – 2a, 2b: Aniq grammatika va imtihon tayyorgarligi

📌 Zamonlar, tushum qoliplari, o‘qib tushunish, eshitib anglash
💰 Haftada 3 kun — 300 000 so‘m
Har kunlik — 600 000 so‘m

⸻

🟠 3 oy – 3a, 3b: Insho, nutq va imtihonlarga tayyorgarlik

🗂 Insholar yozish (sochineie), gapirish ko‘nikmalari (monolog va dialog), grammatikani mukammal o‘rganish
💰 Haftada 3 kun — 420 000 so‘m
Har kunlik — 800 000 so‘m

⸻

🔵 1 oy – Bakalavr va magistratura intervyusiga tayyorgarlik
💰 700 000 so‘m

⸻

🎓 3 oy – A1/A2 rus tili imtihoniga tayyorgarlik

📝 O‘qish, tinglash, test yechish mashg‘ulotlari
💰 Har kunlik — 600 000 so‘m

⸻

📌 Kurs davomiyligi: 3 oydan 9 oygacha

🎯 Natija: O‘qish va ishlash uchun zarur bo‘lgan rus tili darajasiga ega bo‘lish (A2/B1)

🎓 Olish mumkin bo‘lgan sertifikatlar:
• TRKI (TORFL – Test of Russian as a Foreign Language):
A1 – Boshlang‘ich daraja
A2 – Elementar daraja
B1 – O‘rtacha daraja
B2 – Ishlash/o‘qishga tayyor daraja
• Pushkin instituti sertifikati
• Mahalliy imtihon markazlaridan rus tili darajasi sertifikati

📄 Xalqaro sertifikatlar Rossiya universitetlarida o‘qish va Rossiyada rasmiy ishlash uchun amal qiladi!

---

"""
    await message.answer(text=text)
