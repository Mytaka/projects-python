import telebot
from telebot import types

bot = telebot.TeleBot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')

@bot.message_handler(content_types=['photo', 'audio'])
def file(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('delete a photo')
    markup.row(btn1)
    btn2 = types.KeyboardButton('edit',)
    btn3 = types.KeyboardButton('Go to site')
    markup.row(btn2, btn3)
    photo = open('Trifles/photo.jpg', 'rb')
    # file = open('Trifles/text.txt', 'rb')
    # audio = open('Trifles/тривога.mp3', 'rb')
    # video = open('Trifles/video.mp4', 'rb')
    bot.send_photo(message.chat.id, photo)
    # bot.send_document(message.chat.id, file )
    # bot.send_audio(message.chat.id, audio )
    # bot.send_video(message.chat.id, video )
    
    # bot.send_message(message.chat.id, 'What a beautiful photo!', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'delete a photo':
        bot.delete_message(message.chat.id, message.message_id-2)
    

@bot.callback_query_handler(func = lambda callback: True) # если параметр пустой, то возвращаем True
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.infinity_polling()