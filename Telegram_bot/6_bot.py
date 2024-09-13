import telebot
from telebot import types
from currency_converter import CurrencyConverter

bot = telebot.TeleBot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введіть сумму')
    bot.register_next_step_handler(message, summa)

@bot.message_handler()
def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.reply_to(message, 'I NEED FUCKING NUMBER')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EDR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EDR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Another value', callback_data='else')
    else: 
        bot.reply_to(message, 'MATHERFACKER I NEED A NUMBER MORE THEN 0')
        bot.register_next_step_handler(message, summa)
        return
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Chose a pair of money', reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True) 
def callback(call):
    values = call.data.upper().split('/')
    res = currency.convert(amount, values[0], values[1])
    bot.send_message(call.message.chat.id, f'Result: {round(res,2)}')
bot.infinity_polling()