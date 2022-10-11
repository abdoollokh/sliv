from loader import dp
from aiogram import types
from filters.is_tiktok_profile import Is_Tiktok_Profile
from utils import tiktok_parser
import asyncio
import datetime
import random
import json
from keyboards import tiktok_search_result_keyboard
#слито в @smoke_software
@dp.message_handler(Is_Tiktok_Profile())
async def search_tiktok(message: types.Message):
    username = message.text.replace('@', '')
    try:
        # photo = tiktok_parser.get_profile_picture(username)
        loading = await message.answer('<b>Qidirilmoqda... 🔎</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Bazadan qidirilmoqda... ♻️</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>DarkNetdan qidirilmoqda... ♻️</b>')
        await asyncio.sleep(2)
        await loading.delete()
        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2022, 9, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        with open('data/prices.json') as json_file:
            prices = json.load(json_file)
        text = f'''<b>Bazadan topildi ✅</b>\n\n<b>Nik: </b>{username}\n<b>Vzlom qilingan sana: </b>{random_date}\n\n<b>Chernovikdagi videolari: </b>{str(random.randint(3, 20))}\n<b>Yashirilgan videolar: </b>{str(random.randint(3, 20))}\n<b>Telefon raqami: </b>Topildi!'''
        text2 = f'''<b>{username}</b> | {prices["Tiktok_Videos"]} <b>🇷🇺 RUB</b>\n\n<b>🗂 Bu saxifaning barcha ma`lumot, video va rasmlari yuborilishga tayyor.</b>'''
        await message.answer(text)
        await message.answer(text2, reply_markup=tiktok_search_result_keyboard.keyboard)
    except:
        await message.answer('<b>❌ Xatolik yuz berdi, usernameni tekshirib ko`ring...</b>')
