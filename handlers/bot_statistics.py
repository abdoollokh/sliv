from loader import dp
from aiogram import types

@dp.message_handler(text='🌐 Statistika 🌐')
async def stats(message: types.Message):
    await message.answer(f'<b>🔎 Bazadan barcha qidiruvlar soni: 18542</b>\n<b>✅ Botdan xaridlar soni: 6832</b>\n<b>📩 Bot tomonidan yuborilgan xabarlar soni: 61062</b>')
    await message.answer_sticker('CAACAgIAAxkBAAEC3R1hNjNKTzLh2La_N-VGNv8VlqRsFQACSQIAAladvQoqlwydCFMhDiAE')