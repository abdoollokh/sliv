from loader import dp
from aiogram import types
from utils import database
from filters.not_subscribed import Not_Subscribed
from states.subscription import Subscription
import json
from aiogram.dispatcher.storage import FSMContext
from keyboards import social_check_keyboard, menu_keyboard, subscription_check_keyboard

@dp.message_handler(Not_Subscribed())
async def check_subscription(message: types.Message):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    if database.user_exists(message.from_user.id):
        await message.answer(f'💡Botdam to`liq foydalanish uchun kanalimizga obuna bo`l, u yerdan bazadan doimi video fotolar 🔞 yuklanib boriladi. Obuna bo`lgandan so`ng bu tugmani bos - «Obuna bo`ldim»👇\n\n{config["Bot_Data"]["Channel_Link"]}', reply_markup=subscription_check_keyboard.keyboard)
        await Subscription.waiting.set()
    else:
        database.create_user(message.from_user.id, message.from_user.username)
        await message.answer(f'💡Botdam to`liq foydalanish uchun kanalimizga obuna bo`l, u yerdan bazadan doimi video fotolar 🔞 yuklanib boriladi. Obuna bo`lgandan so`ng bu tugmani bos - «Obuna bo`ldim»👇\n\n{config["Bot_Data"]["Channel_Link"]}', reply_markup=subscription_check_keyboard.keyboard)
        await Subscription.waiting.set()

@dp.message_handler(state=Subscription.waiting)
async def answer_while_waiting(message: types.Message, state: FSMContext):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    if config['Bot_Data']['Subscription_Required']:
        await message.answer(f'💡Botdam to`liq foydalanish uchun kanalimizga obuna bo`l, u yerdan bazadan doimi video fotolar 🔞 yuklanib boriladi. Obuna bo`lgandan so`ng bu tugmani bos - «Obuna bo`ldim»👇\n\n{config["Bot_Data"]["Channel_Link"]}', reply_markup=subscription_check_keyboard.keyboard)
    else:
        await state.finish()
        text = f'''👋 Salom, {message.from_user.full_name}\n\nBu bot har qanda qizning ijtimoiy tarmoqdagi profillari orqali shaxsiy ma`lumotlarini, yoki 🔞 rasm, videolarini topib beradi  😏\n\n🔎 Botga Instagram, Vkontakte yoki Telefon raqamni (Whatsapp, Telegram, Viberdan qidirsh uchun) yuboring  🔞👇'''
        photo='https://i.postimg.cc/x14b1PV7/start.png'
        await message.answer_photo(photo, text, reply_markup=menu_keyboard.keyboard)
        await message.answer('🔥 Qayerdan izlashimizni tanlang', reply_markup=social_check_keyboard.keyboard)

@dp.callback_query_handler(text='check_subscribtion', state=Subscription.waiting)
async def check_subscribtion(callback: types.CallbackQuery, state: FSMContext):
    if database.get_user(callback.from_user.id)['subscribed']:
        await callback.message.delete()
        text = f'''👋 Salom, {callback.message.from_user.full_name}\n\nBu bot har qanda qizning ijtimoiy tarmoqdagi profillari orqali shaxsiy ma`lumotlarini, yoki 🔞 rasm, videolarini topib beradi  😏\n\n🔎 Botga Instagram, Vkontakte yoki Telefon raqamni (Whatsapp, Telegram, Viberdan qidirsh uchun) yuboring  🔞👇'''
        photo='https://i.postimg.cc/x14b1PV7/start.png'
        await callback.message.answer_photo(photo, text, reply_markup=menu_keyboard.keyboard)
        await callback.message.answer('🔥 Qayerdan izlashimizni tanlang', reply_markup=social_check_keyboard.keyboard)
        await state.finish()
    else:
        await callback.answer('Siz obuna bo`lmadingiz!')

@dp.chat_member_handler(state='*')
async def handle_channel_actions(chat_member: types.ChatMemberUpdated):
    if chat_member.old_chat_member.status == 'left' and (chat_member.new_chat_member.status == 'member' or chat_member.new_chat_member.status == 'creator'):
        database.update_user(chat_member.from_user.id, 'subscribed', 1)
    elif chat_member.old_chat_member.status == 'member' and chat_member.new_chat_member.status == 'left':
        database.update_user(chat_member.from_user.id, 'subscribed', 0)