import telebot
import sqlite3

bot = telebot.TeleBot('7212369705:AAEiFdsylqZwdkyDchuRlxtYhzz6NiNE3Nw')

# name = None

@bot.message_handler(commands=['start'])
def main(message):
    conn = sqlite3.connect('4_bot.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Hello, give me your name')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    # global name
    name = message.text.strip()
    bot.send_message(message.chat.id,'Give me your pass'  )
    bot.register_next_step_handler(message, user_pass, name)

def user_pass(message, name):

    password = message.text.strip()
    conn = sqlite3.connect('4_bot.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name,pass) VALUES ("%s","%s")' %(name, password))
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('List', callback_data='users'))
    bot.send_message(message.chat.id,'You are check in',  reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    conn = sqlite3.connect('4_bot.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    

    info = " "

    i = 1
    for el in users:
        info += f"{i}) name {el[1]}, pass {el[2]}\n"
        i += 1

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.infinity_polling()

