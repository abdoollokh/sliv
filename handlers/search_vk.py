from loader import dp
from aiogram import types
from utils import vk_parser
import asyncio
import datetime
import json
import random
from filters.is_vk_link import Is_Vk_Link
from keyboards import search_result_keyboard

@dp.message_handler(Is_Vk_Link())
async def search_vk(message: types.Message):
    try:
        user_id = message.text.split('vk.com')[1].replace('/', '')
        user_data = vk_parser.get_user_data(user_id)
        if user_data['sex'] == 1:
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
            photo = user_data['photo']
            text = f'''<b>Bazadan topildi ✅</b>\n\n<b>id: </b>{user_data["id"]}\n<b>Ism: </b>{user_data["first_name"]}\n<b>Familiya: </b>{user_data["last_name"]}\n<b>Vzlom qilingan sana: </b>{random_date}\n\n<b>Yozishmalar: </b>{str(random.randint(30, 98))}\n<b>🔞 rasmlar: </b>Topildi ✅\n<b>🔞 videolar: </b>Topildi ✅'''
            text2 = f'''<b>{user_data["first_name"]} {user_data["last_name"]}</b> | {prices["Archive"]} <b>🇷🇺 RUB</b>\n\n<b>🗂 Yuborilgan profil egasinig bazdagi 🔞 rasm, video va yozishmalari yuborilishga tayyor.</b>'''
            await message.answer_photo(photo, text)
            await message.answer(text2, reply_markup=search_result_keyboard.keyboard)
        else:
            loading = await message.answer('<b>Qidirilmoqda... 🔎</b>')
            await asyncio.sleep(2)
            await loading.edit_text('<b>Bazadan qidirilmoqda... ♻️</b>')
            await asyncio.sleep(2)
            await loading.edit_text('<b>DarkNetdan qidirilmoqda... ♻️</b>')
            await asyncio.sleep(2)
            await loading.edit_text('<b>❌ Bazadan topilmadi</b>')
            await message.answer_sticker('CAACAgQAAxkBAAEC3SNhNkNNMD7XRzYZ6uhRnCsB3uNz8AACCQgAAiQWWVI_eK9jUmCxFSAE')
    except:
        await message.answer('<b>❌ Xatolik yuz berdi, ssilkani tekshirib ko`ring...</b>')
