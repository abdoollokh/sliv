from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
instagram = types.InlineKeyboardButton('Instagram', callback_data='instagram')
vk = types.InlineKeyboardButton('Vkontakte', callback_data='vk')
phone_number = types.InlineKeyboardButton('Telefon raqami', callback_data='phone_number')
tiktok = types.InlineKeyboardButton('TikTok', callback_data='tiktok')
keyboard.add(instagram, vk, phone_number, tiktok)

back_keyboard = types.InlineKeyboardMarkup()
back_button = types.InlineKeyboardButton('Orqaga', callback_data='social_back')
back_keyboard.add(back_button)