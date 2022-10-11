from loader import dp
from aiogram import types
from utils import database

@dp.message_handler(text='🤑 Do`stingni taklif qil 🤑')
async def referals(message: types.Message):
    count = database.get_user_referals_count(message.from_user.id)
    balance = database.get_user(message.from_user.id)['balance']
    username = (await message.bot.me).username
    text = f'''<b>Sizninh referal ssilkangiz:</b>\nhttps://t.me/{username}?start={message.from_user.id}\n\n<b>Taklif qilinganlar soni: </b><code>{count}</code>\n<b>Xisob: </b><code>{balance}</code>\n\n<i>Do`stlaringizni taklif qiling va ularning xarididan 50% xisobingizga oling!</i>\n\nReferal xisobdan yechib olish uchun, bu buyruqni bering /pay'''
    await message.answer(text)
