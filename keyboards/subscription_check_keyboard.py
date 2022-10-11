from aiogram import types

keyboard = types.InlineKeyboardMarkup()
check = types.InlineKeyboardButton('Obuna bo`ldim', callback_data='check_subscribtion')
keyboard.add(check)