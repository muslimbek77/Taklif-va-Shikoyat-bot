from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

taklif_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Taklif va shikoyat"),
            KeyboardButton(text="Biz haqimizda"),
        ],
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)