from aiogram import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
find_leaks = types.KeyboardButton('π Bazadan qidirish π')
help = types.KeyboardButton('π¨πΌβπ§ Bog`lanish π¨πΌβπ§')
referals = types.KeyboardButton('π€ Do`stingni taklif qil π€')
examples = types.KeyboardButton('π‘Bot qanday ishlaydiπ‘')
statistics = types.KeyboardButton('π Statistika π')
keyboard.row(find_leaks)
keyboard.row(help)
keyboard.row(referals)
keyboard.row(examples, statistics)