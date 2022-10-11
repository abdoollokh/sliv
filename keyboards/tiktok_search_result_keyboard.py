from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
videos = types.InlineKeyboardButton('💳 Videolarni sotib olish', callback_data='buy_tiktok_archive')
phone = types.InlineKeyboardButton('📱 Telefon raqamini sotib olish', callback_data='buy_phone')
keyboard.add(videos, phone)