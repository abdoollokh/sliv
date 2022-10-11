from aiogram import types
import json

def keyboard():
    kb = types.InlineKeyboardMarkup(1)
    mapping = {'Archive': 'Rasmlar arxivi', 'Photo': 'Rasm', 'Unlimited_1': '1 kun cheksiz', 'Unlimited_7': '7 kun cheksiz', 'Unlimited_30': '30 kun cheksiz', 'Phone_Number_Info': 'Telefon raqam haqida ma`lumot', 'Messages_Archive': 'Xabar', 'Phone_Number': 'Raqamni qidirish', 'Hidden_Friends': 'Yashirin do`stlar', 'Phone_Number_Leaks': 'Raqam orqali arxiv', 'Tiktok_Videos': 'TT arxivi'}
    with open('data/prices.json') as json_file:
        prices = json.load(json_file)
    for price in prices:
        button = types.InlineKeyboardButton(f'{mapping[price]} | {prices[price]}₽', callback_data=f'edit:{price}')
        kb.add(button)
    cancel = types.InlineKeyboardButton('Bekor qilish', callback_data='return')
    kb.add(cancel)
    return kb