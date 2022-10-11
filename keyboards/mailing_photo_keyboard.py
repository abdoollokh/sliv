from aiogram import types

keyboard = types.InlineKeyboardMarkup(2)
dont_add_photo = types.InlineKeyboardButton('Rasm qo`shmaslik', callback_data='no_photo')
cancel = types.InlineKeyboardButton('Bekor qilish', callback_data='return')
keyboard.add(dont_add_photo, cancel)