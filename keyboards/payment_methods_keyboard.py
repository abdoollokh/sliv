from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
qiwi = types.InlineKeyboardButton('🥝 QIWI | 💳 karta', callback_data='method_qiwi')
yoo = types.InlineKeyboardButton('YOOMONEY | 💳 karta', callback_data='method_yoo')
back = types.InlineKeyboardButton('Orqaga', callback_data='cancel_payment')
keyboard.add(qiwi, yoo, back)