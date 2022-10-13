from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
archive = types.InlineKeyboardButton('💳 Arxiv (barcha rasm va videolar) sotib olish', callback_data='buy_archive')
photo = types.InlineKeyboardButton('🍑 Bitta rasm sotib olish', callback_data='buy_photo')
phone = types.InlineKeyboardButton('📱 Telefon raqamini topish', callback_data='buy_phone')
messages = types.InlineKeyboardButton('🔞 Yozishmalarni sotib olish', callback_data='buy_messages')
unlimited = types.InlineKeyboardButton('🔎 Cheksiz qidiruv', callback_data='buy_unlimited')
keyboard.add(archive, photo, messages, phone, unlimited)
