from loader import dp
from aiogram import types
import json

@dp.message_handler(text='👨🏼‍🔧 Bog`lanish 👨🏼‍🔧')
async def help(message: types.Message):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    username = config['Bot_Data']['Help_Username']
    keyboard = types.InlineKeyboardMarkup()
    button_acc = types.InlineKeyboardButton(text='💞 Admin', url=f't.me/{username}', callback_data='help')
    keyboard.add(button_acc)
    await message.answer('🍓 Texnik yordam 👇', reply_markup=keyboard)
    await message.answer_sticker('CAACAgIAAxkBAAEC3R9hNjNUj-nang5taLVR7eGvkDXcjQACOAsAAk7kmUsysUfS2U-M0CAE')