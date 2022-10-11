import asyncio
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp, bot
from utils import edit_config, edit_price
from filters.is_admin import Is_Admin
import json
from utils import database, qiwi
from keyboards import admin_keyboard, back_button_keyboard, mailing_photo_keyboard, prices_keyboard, admin_ids_keyboard
from states.admin import Admin
import sqlite3
#слито в @smoke_software
@dp.message_handler(Is_Admin(), commands=['admin'])
async def admin(message: types.Message):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)

@dp.callback_query_handler(text='return', state='*')
async def back(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await callback.message.edit_text(text, reply_markup=admin_keyboard.keyboard)

@dp.callback_query_handler(text='mailing')
async def wait_mailing_text(callback: types.CallbackQuery):
    await callback.message.edit_text('Ssilkani yozing...', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_text.set()

@dp.message_handler(state=Admin.wait_for_text)
async def wait_for_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await message.answer('Rasmni yuboring...', reply_markup=mailing_photo_keyboard.keyboard)
    await Admin.wait_for_picture.set()

@dp.message_handler(state=Admin.wait_for_picture, content_types=['photo'])
async def mail(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        text = data['text']
    photo = message.photo[-1].file_id
    users = database.get_all_users_ids()
    counter = 0
    errs = 0
    count_msg = await message.answer(f'Xabar yuborildi: {counter}')
    err_msg = await message.answer(f'Xato: {errs}')
    for user in users:
        try:
            await bot.send_photo(user[0], photo, text)
            counter += 1
            if counter % 100 == 0:
                await count_msg.edit_text(f'Xabar yuborildi: {counter}')
        except:
            errs += 1
            if errs % 100 == 0:
                await err_msg.edit_text(f'Xato: {errs}')
    await message.answer(f'<b>Xabar muvaffaqyatli yuborildi: </b><code>{counter}</code>')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()

@dp.callback_query_handler(state=Admin.wait_for_picture, text='no_photo')
async def text_mailing(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data['text']
    users = database.get_all_users_ids()
    counter = 0
    errs = 0
    count_msg = await callback.message.answer(f'Xabar yuborildi: {counter}')
    err_msg = await callback.message.answer(f'Xato: {errs}')
    await state.finish()
    for user in users:
        try:
            await bot.send_message(user[0], text)
            counter += 1
            if counter % 100 == 0:
                await count_msg.edit_text(f'Xabar yuborildi: {counter}')
        except:
            errs += 1
            if errs % 100 == 0:
                await err_msg.edit_text(f'Xato: {errs}')
    await callback.message.answer(f'<b>Xabar muvaffaqyatli yuborildi: </b><code>{counter}</code>')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await callback.message.answer(text, reply_markup=admin_keyboard.keyboard)

@dp.callback_query_handler(text='statistics')
async def send_stats(callback: types.CallbackQuery):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    total_purchases = config['Statistics']['Purchases']
    total_earned = config['Statistics']['Total_Earned']
    total_users = len(database.get_all_users_ids())
    referals_balances = database.get_balances_sum()
    text = f'<b>Statistika:</b>\n\n<b>Foydalanuvchilar: </b><code>{total_users}</code>\n<b>Xarid: </b><code>{total_purchases}</code>\n<b>Ishlandi: </b><code>{total_earned} RUB</code>\n<b>Raferal xisobi: </b><code>{referals_balances} RUB</code>'
    await callback.message.edit_text(text, reply_markup=back_button_keyboard.keyboard)

@dp.callback_query_handler(text='update_prices')
async def category_to_edit(callback: types.CallbackQuery):
    await callback.message.edit_text('Tanlang, qaysi narhni o`zgartirishni:', reply_markup=prices_keyboard.keyboard())
    await Admin.wait_for_category.set()

@dp.callback_query_handler(state=Admin.wait_for_category)
async def new_price(callback: types.CallbackQuery, state: FSMContext):
    type = callback.data.replace('edit:', '')
    async with state.proxy() as data:
        data['type'] = type
    await callback.message.edit_text('Yangi narxni yuboring...', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_price.set()

@dp.message_handler(state=Admin.wait_for_price)
async def update_price(message: types.Message, state: FSMContext):
    try:
        price = int(message.text)
        async with state.proxy() as data:
            type = data['type']
        edit_price.edit_price(type, price)
        await message.answer('Narx o`zgartirildi!')
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        help_account = config['Bot_Data']['Help_Username']
        channel_link = config['Bot_Data']['Channel_Link']
        if config['Bot_Data']['Subscription_Required']:
            subscription_required = 'Xa'
        else:
            subscription_required = 'Yo`q'
        referal_percentage = config['Bot_Data']['Referal_Percentage']
        text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
        await message.answer(text, reply_markup=admin_keyboard.keyboard)
        await state.finish()
    except:
        await message.answer('Siz raqam yubormadingiz', reply_markup=back_button_keyboard.keyboard)

@dp.callback_query_handler(text='update_qiwi')
async def wait_for_qiwi(callback: types.CallbackQuery):
    await callback.message.edit_text('Qiwi ma`lumotlarini bunday shaklda yuboring\nRaqam:ТОКЕН:NikНЕЙМ\n791xxxxxxxx:123456qwerty:USERNAME123', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_qiwi.set()

@dp.message_handler(state=Admin.wait_for_qiwi)
async def update_qiwi(message: types.Message, state: FSMContext):
    number = message.text.split(':')[0]
    token = message.text.split(':')[1]
    nickname = message.text.split(':')[2]
    edit_config.edit_qiwi(number, token, nickname)
    await message.answer('Qiwi o`zgartirildi!')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()

@dp.callback_query_handler(text='update_help_link')
async def wait_link(callback: types.CallbackQuery):
    await callback.message.edit_text('Yangi admin akkauntini yuboring...', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_username.set()

@dp.message_handler(state=Admin.wait_for_username)
async def set_link(message: types.Message, state: FSMContext):
    edit_config.edit_help_username(message.text)
    await message.answer('Akkaunt o`zgartirildi!')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()

@dp.callback_query_handler(text='update_percentage')
async def wait_percentage(callback: types.CallbackQuery):
    await callback.message.edit_text('Yangi referal foizini bu shaklda yuboring...\n(0.01 = 1%, 1 = 100%)', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_percentage.set()

@dp.message_handler(state=Admin.wait_for_percentage)
async def update_percentage(message: types.Message, state: FSMContext):
    try:
        edit_config.edit_referal_percentage(float(message.text))
        await message.answer('Foiz o`zgartirildi!')
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        help_account = config['Bot_Data']['Help_Username']
        channel_link = config['Bot_Data']['Channel_Link']
        if config['Bot_Data']['Subscription_Required']:
            subscription_required = 'Xa'
        else:
            subscription_required = 'Yo`q'
        referal_percentage = config['Bot_Data']['Referal_Percentage']
        text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
        await message.answer(text, reply_markup=admin_keyboard.keyboard)
        await state.finish()
    except:
        await message.answer('Siz raqam yubormadingiz', reply_markup=back_button_keyboard.keyboard)

@dp.callback_query_handler(text='update_channel_link')
async def wait_channel_link(callback: types.CallbackQuery):
    await callback.message.edit_text('Yangi kanal ssilkasini yuboring', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_link.set()

@dp.message_handler(state=Admin.wait_for_link)
async def update_percentage(message: types.Message, state: FSMContext):
    edit_config.edit_channel_link(message.text)
    await message.answer('Ssilka o`zgartirildi!')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()

@dp.callback_query_handler(text='switch_subscription_check')
async def wait_channel_link(callback: types.CallbackQuery):
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    required = config['Bot_Data']['Subscription_Required']
    edit_config.edit_subscription_required(not required)
    await asyncio.sleep(1)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if not config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await callback.message.delete()
    await callback.message.answer(text, reply_markup=admin_keyboard.keyboard)

@dp.callback_query_handler(text='add_admin')
async def wait_channel_link(callback: types.CallbackQuery):
    await callback.message.edit_text('Idni yuboring', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_admin_id.set()

@dp.message_handler(state=Admin.wait_admin_id)
async def update_percentage(message: types.Message, state: FSMContext):
    try:
        edit_config.add_admin(int(message.text))
        await message.answer('Admin qo`shildi!')
        with open('data/config.json') as json_file:
            config = json.load(json_file)
        help_account = config['Bot_Data']['Help_Username']
        channel_link = config['Bot_Data']['Channel_Link']
        if config['Bot_Data']['Subscription_Required']:
            subscription_required = 'Xa'
        else:
            subscription_required = 'Yo`q'
        referal_percentage = config['Bot_Data']['Referal_Percentage']
        text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
        await message.answer(text, reply_markup=admin_keyboard.keyboard)
        await state.finish()
    except:
        await message.answer('Siz ID yubormadingiz', reply_markup=back_button_keyboard.keyboard)

@dp.callback_query_handler(text='remove_admin')
async def wait_channel_link(callback: types.CallbackQuery):
    await callback.message.edit_text('O`chirmoqchi bo`lgan idni yuboring', reply_markup=admin_ids_keyboard.keyboard())
    await Admin.wait_admin_id_remove.set()

@dp.callback_query_handler(state=Admin.wait_admin_id_remove)
async def update_percentage(callback: types.CallbackQuery, state: FSMContext):
    edit_config.delete_admin(int(callback.data))
    await callback.message.answer('Admin o`chirib yuborildi!')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await callback.message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()

@dp.callback_query_handler(text='qiwi_balance')
async def balance(callback: types.CallbackQuery):
    await callback.message.answer(f'<b>Xisob: </b><code>{qiwi.get_balance()}Р.</code>')

@dp.callback_query_handler(text='show_referals')
async def referals(callback: types.CallbackQuery):
    text = ''
    for i in database.get_referals():
        text += f'{i}({database.get_user(i)["username"]}) | {database.get_referals()[i]} | {int(database.get_user(i)["balance"])}Р.\n'
    await callback.message.edit_text(text, reply_markup=back_button_keyboard.keyboard)

@dp.callback_query_handler(text='update_yoo')
async def wait_for_qiwi(callback: types.CallbackQuery):
    await callback.message.edit_text('Qabul qiluvchi xisob raqamini yuboring\nXisobda uvedomleniya ssilkasini bu shaklda ko`rsatishni unutmang (ip сервера):9000/yoomoney\nip bez skobok ko`rsating', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_yoo.set()

@dp.message_handler(state=Admin.wait_for_yoo)
async def update_qiwi(message: types.Message, state: FSMContext):
    reciver = message.text
    edit_config.edit_yoo(reciver)
    await message.answer('YOOMONEY успешно изменен!')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()

@dp.callback_query_handler(text='update_percentage_ind')
async def wait_for_qiwi(callback: types.CallbackQuery):
    await callback.message.edit_text('Ma`lumotlarni bunday shaklda yuboring:\nUser:FOIZ\nFoizni bu shaklda yuboring (0.01 = 1%, 0.5 = 50%, 1 = 100%)', reply_markup=back_button_keyboard.keyboard)
    await Admin.wait_for_percentage_ind.set()

@dp.message_handler(state=Admin.wait_for_percentage_ind)
async def update_qiwi(message: types.Message, state: FSMContext):
    user = message.text.split(':')[0]
    percentage = message.text.split(':')[1]
    con = sqlite3.connect('data/bot.db')
    cur = con.cursor()
    cur.execute(f'UPDATE users SET percentage = "{percentage}" WHERE username = "{user}"')
    con.commit()
    await message.answer('Foiz o`zgartirildi!')
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    help_account = config['Bot_Data']['Help_Username']
    channel_link = config['Bot_Data']['Channel_Link']
    if config['Bot_Data']['Subscription_Required']:
        subscription_required = 'Xa'
    else:
        subscription_required = 'Yo`q'
    referal_percentage = config['Bot_Data']['Referal_Percentage']
    text = f'''<b>Ma`muriyat:</b>\n\n<b>Akkaunt TP: </b><code>@{str(help_account)}</code>\n<b>Kanal ssilkasi: </b><code>{str(channel_link)}</code>\n<b>Obunani tekshirish: </b><code>{str(subscription_required)}</code>\n<b>Referallar foizi: </b><code>{str(referal_percentage*100)}%</code>'''
    await message.answer(text, reply_markup=admin_keyboard.keyboard)
    await state.finish()
    