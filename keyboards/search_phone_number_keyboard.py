from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
leaks = types.InlineKeyboardButton('🔎 Bazadan tekshirish', callback_data='phone_leaks')
info = types.InlineKeyboardButton('🔎 Shaxsiy ma`lumotlarni qidirish', callback_data='phone_info')
keyboard.add(leaks, info)