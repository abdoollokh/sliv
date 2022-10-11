from aiogram import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
find_leaks = types.KeyboardButton('🔍 Bazadan qidirish 🔍')
help = types.KeyboardButton('👨🏼‍🔧 Bog`lanish 👨🏼‍🔧')
referals = types.KeyboardButton('🤑 Do`stingni taklif qil 🤑')
examples = types.KeyboardButton('💡Bot qanday ishlaydi💡')
statistics = types.KeyboardButton('🌐 Statistika 🌐')
keyboard.row(find_leaks)
keyboard.row(help)
keyboard.row(referals)
keyboard.row(examples, statistics)