from aiogram import types

keyboard = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton('Orqaga', callback_data='return')
keyboard.add(button)