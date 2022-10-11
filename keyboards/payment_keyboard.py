from aiogram import types

def make_keyboard(url: str, type: str, pref = ''):
    keyboard = types.InlineKeyboardMarkup(1)
    link = types.InlineKeyboardButton('💳 To`lovga o`tish', callback_data='procced_payment', url=url)
    check = types.InlineKeyboardButton('🔄 To`lovni tekshirish', callback_data=f'{pref}check_payment_{type}')
    cancel = types.InlineKeyboardButton('❌ Bekor qilish', callback_data='cancel_payment')
    keyboard.add(link, check, cancel)
    return keyboard