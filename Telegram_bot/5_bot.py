import telebot
import requests
import json

bot = telebot.TeleBot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')
API = '53e3133e93f444e7b908851caa9af167'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, nice to see you. Where are you from?')
    

@bot.message_handler(content_types=['text'])
def conteny_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message, f'Weather forecast: {data["main"]["temp"]}')
    else: 
        bot.send_message(message.chat.id, 'Incorrect city name')

    
bot.infinity_polling()

