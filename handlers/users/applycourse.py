from aiogram.types import Message,CallbackQuery
from loader import dp,db,bot
from aiogram import F
from aiogram.fsm.context import FSMContext 
from states.reklama import ApplyCourseState
from data.config import MY_GROUP


@dp.callback_query(F.data.startswith("apply_"))
async def start_application(call: CallbackQuery, state: FSMContext):
    course = call.data.replace("apply_", "")  
    await state.update_data(course=course)

    await call.message.answer("👤 Ism familiyangizni kiriting:")
    await state.set_state(ApplyCourseState.full_name)

@dp.message(ApplyCourseState.full_name)
async def get_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("📅 Yoshingizni kiriting:")
    await state.set_state(ApplyCourseState.age)

@dp.message(ApplyCourseState.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("📞 Telefon raqamingizni yuboring:")
    await state.set_state(ApplyCourseState.phone)

@dp.message(ApplyCourseState.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("📆 Qaysi kunlar sizga qulay? (Masalan: Dush, Chor, Ju)")
    await state.set_state(ApplyCourseState.schedule)

@dp.message(ApplyCourseState.schedule)
async def get_schedule(message: Message, state: FSMContext):
    await state.update_data(schedule=message.text)
    await message.answer("🕰 Qaysi vaqt qulay? (Abetgacha / Abetdan keyin)")
    await state.set_state(ApplyCourseState.time_preference)

@dp.message(ApplyCourseState.time_preference)
async def get_time_preference(message: Message, state: FSMContext):
    await state.update_data(time_preference=message.text)
    await message.answer("📚 Kurs bo‘yicha darajangiz? (0 dan boshlayman / Avval o‘qiganman)")
    await state.set_state(ApplyCourseState.level)

@dp.message(ApplyCourseState.level)
async def finish_application(message: Message, state: FSMContext):
    await state.update_data(level=message.text)
    data = await state.get_data()

    text = (
        "📝 <b>Backend kursiga yangi ariza:</b>\n\n"
        f"👤 Ism: {data['full_name']}\n"
        f"📅 Yosh: {data['age']}\n"
        f"📞 Telefon: {data['phone']}\n"
        f"📆 Kuni: {data['schedule']}\n"
        f"🕰 Vaqti: {data['time_preference']}\n"
        f"📚 Darajasi: {data['level']}"
    )

    # Foydalanuvchiga rahmat xabari
    await message.answer("✅ Arizangiz qabul qilindi! Tez orada bog‘lanamiz.")

    # Adminlarga yuborish
    await message.bot.send_message(MY_GROUP, text, parse_mode="HTML")

    await state.clear()
