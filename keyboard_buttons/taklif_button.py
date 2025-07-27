from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

taklif_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Bizning kurslar"),
            KeyboardButton(text="🏢 Renessans Agency"),
        ],
        [
            KeyboardButton(text="📩 Murojaat"),
            KeyboardButton(text="ℹ️ Biz haqimizda"),
        ],
        [KeyboardButton(text="🌐 Ijtimoiy tarmoqlarda biz")],
        [KeyboardButton(text="📍 Bizning Manzil")],
        
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Menudan birini tanlang"
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

our_course_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Asosiy menyuga qaytish")],
        [KeyboardButton(text="🛡️ Kiberxavfsizlik"), KeyboardButton(text="📱 Mobil dasturlash (Flutter)")],
        [KeyboardButton(text="💻 Backend"), KeyboardButton(text="🎨 Frontend")],
        [KeyboardButton(text="🖌️ Grafik Dizayner"), KeyboardButton(text="🎭 Shaxsiy Brend (Face Brend)")],
        [KeyboardButton(text="🎥 Videografiya"), KeyboardButton(text="📚 Matematika")],
        [KeyboardButton(text="🇸🇦 Arab tili"), KeyboardButton(text="🇬🇧 Ingliz tili")],
        [KeyboardButton(text="🇩🇪 Nemis tili"), KeyboardButton(text="🇰🇷 Koreys tili")],
        [KeyboardButton(text="🇷🇺 Rus tili")],
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Kurslardan birini tanlang"
)
