from loader import dp
from aiogram import types
from filters.is_phone_number import Is_Phone_Number
import json
from keyboards import search_phone_number_keyboard

@dp.message_handler(Is_Phone_Number())
async def search_phone_number(message: types.Message):
    with open('data/prices.json') as json_file:
        prices = json.load(json_file)
        price = prices['Phone_Number']
    number = message.text.split(' ')[0]
    text = f'''<b>⚙ Foydalanuvchi:\n\n💬 Raqam {number}\n\n</b>➖➖➖➖➖➖➖➖➖➖➖\n\n<i>🔞 Shaxsiy rasmlar: ?\n⛔ Yashirin ma`lumotlar: ?\n👥 Foydalanuvchining ijtimoiy tarmoqdagi saxifalari: ?</i>\n\n<b>💰 Tekshiruv narxi: {price} RUB💳</b>'''
    await message.answer(text, reply_markup=search_phone_number_keyboard.keyboard)