from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
        [ KeyboardButton(text="🎭 Shaxsiy Brend (Face brand)"),KeyboardButton(text="🎯 Target (Reklama Sozlash)")],
        [KeyboardButton(text="🎥 Videografiya"),KeyboardButton(text="🖌️ Grafik Dizayner") ],
        [KeyboardButton(text="🇸🇦 Arab tili"), KeyboardButton(text="🇬🇧 Ingliz tili")],
        [KeyboardButton(text="🇩🇪 Nemis tili"), KeyboardButton(text="🇰🇷 Koreys tili")],
        [KeyboardButton(text="🇷🇺 Rus tili"),KeyboardButton(text="📚 Matematika")],
    ],
    resize_keyboard=True,
    input_field_placeholder="👇 Kurslardan birini tanlang"
)



social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📱 Telegram", url="https://t.me/Renessans_Uzbekistan3")],
        [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/3renessans_uzbekistan")],
        [InlineKeyboardButton(text="▶️ YouTube", url="https://www.youtube.com/@3RenessansUzbekistan")],
        [InlineKeyboardButton(text="🌐 Veb-sayt", url="https://3renessans.uz")],

    ]
)
