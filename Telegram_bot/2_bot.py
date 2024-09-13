import telebot
import webbrowser

bot = telebot.TeleBot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')

@bot.message_handler(commands=['site'])
def site(message):
   webbrowser.open('https://keep.google.com/u/0/#label/Telegram_Bot')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')

@bot.message_handler(commands=['1'])
def main(message):
    bot.send_message(message.chat.id, '<b>/1) Алгоритми та методи обчислень</b>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'world':
        bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(non_stop=True)



