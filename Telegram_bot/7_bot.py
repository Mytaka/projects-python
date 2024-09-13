from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')
dp = Dispatcher(bot)

@dp.message_heandler(commands=['start']) # content_types=['text','video','photo']
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    # await message.reply('Hello')
    # await message.answer_photo()
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('delete a photo', callback_data='delete')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('edit', callback_data='edit')
    btn3 = types.InlineKeyboardButton('Go to site', url = 'https://jut.su/anime/ongoing/')
    markup.row(btn2, btn3)
    bot.reply(message, 'What a beautiful photo!', reply_markup = markup)
    

@dp.callback_quary_heandler()
async def callback(call):
    await call.message.answer('Da')


@dp.message_heandler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.InlineKeyboardMarkup(one_time_keyboard=True) #что бы кнопки исчезаили при нажатии
    



executor.start_poling(dp)
