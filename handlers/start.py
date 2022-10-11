from loader import dp, bot, zalety
from aiogram import types
from utils import database
from keyboards import menu_keyboard, social_check_keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f'''👋 Salom, {message.from_user.full_name}\n\nBu bot har qanda qizning ijtimoiy tarmoqdagi profillari orqali shaxsiy ma`lumotlarini, yoki 🔞 rasm, videolarini topib beradi  😏\n\n🔎 Botga Instagram, Vkontakte yoki Telefon raqamni (Whatsapp, Telegram, Viberdan qidirsh uchun) yuboring  🔞👇'''
    photo='https://i.postimg.cc/x14b1PV7/start.png'
    if not database.user_exists(message.from_user.id):
        database.create_user(message.from_user.id, message.from_user.username)
        if message.get_args() != '':
            if database.user_exists(message.get_args()):
                database.update_user(message.from_user.id, 'invited_by', message.get_args())
        await message.answer_photo(photo, text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Qayerdan izlashimizni tanlang', reply_markup=social_check_keyboard.keyboard)
        await bot.send_message(zalety, f"Sizda yangi referal {message.from_user.full_name}")
    else:
        await message.answer_photo(photo, text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Qayerdan izlashimizni tanlang', reply_markup=social_check_keyboard.keyboard)
        await bot.send_message(zalety, f"Sizda yangi referal {message.from_user.full_name}")

