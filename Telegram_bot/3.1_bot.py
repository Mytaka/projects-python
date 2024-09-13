import telebot
from telebot import types

bot = telebot.TeleBot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')

@bot.message_handler(content_types=['photo', 'audio'])
def file(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('delete a photo', callback_data='delete')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('edit', callback_data='edit')
    btn3 = types.InlineKeyboardButton('Go to site', url = 'https://jut.su/anime/ongoing/')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a beautiful photo!', reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True) # если параметр пустой, то возвращаем True
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.infinity_polling()


