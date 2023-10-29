import telebot
import requests
import random
import nltk
import threading
import time

nltk.download('words')
english_words = set(nltk.corpus.words.words())

bot = telebot.TeleBot("6324369008:AAEfJEjHJW2_VozhQUdQLuixXJ-2X4ulzgs")
bot_state = 'running'

def check_words():
    global bot_state

    while bot_state == 'running':
        word = random.choice(list(english_words))
        url = f"https://t.me/{word}"
        req = requests.get(url).text

        if '"tgme_username_link"' in req:
            print(f"Done | {word}")
            with open('main.txt', 'a') as f:
                f.write(word + '\n')
        else:
            print(f"Error | {word}")
            with open('man.txt', 'a') as f:
                f.write(word + '\n')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    button_check = telebot.types.InlineKeyboardButton(text='Check 🫦', callback_data='check')
    button_stop = telebot.types.InlineKeyboardButton(text='Stop 🎟️', callback_data='stop')
    button_send = telebot.types.InlineKeyboardButton(text='Send File 1 💅🏻', callback_data='send')
    h1 = telebot.types.InlineKeyboardButton(text='Send File 2 💅🏻', callback_data='send1') 
    del1 = telebot.types.InlineKeyboardButton(text='Delete List 1 🐝', callback_data='delete')
    del2 = telebot.types.InlineKeyboardButton(text='Delete List 2 🐝', callback_data='delete2')
    markup.add(button_check, button_stop, button_send, h1, del1, del2)
    bot.send_message(message.chat.id,'''Welcome to make list meaning words language english to start press check!🥷🏻''',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global bot_state

    if call.data == 'check':
        if bot_state == 'running':
            bot.send_message(call.message.chat.id, "Done Run Bot✅.")
            t = threading.Thread(target=check_words)
            t.start()
    elif call.data == 'stop':
      bot_state = 'stopped'
      time.sleep(1)
      bot.send_message(call.message.chat.id, "Bot stopped .")
      bot_state = 'running'


    elif call.data == 'send':
        with open('main.txt', 'rb') as f:
            bot.send_document(call.message.chat.id, f, caption='Available or Blocked 🦧')
    elif call.data == 'send1':
        with open('man.txt', 'rb') as f:
            bot.send_document(call.message.chat.id, f, caption='this all username not available 🕷️')
    elif call.data == 'delete':
      with open('main.txt', 'w') as f:
        f.write('')
      bot.send_message(call.message.chat.id, "List 1 deleted 📜")

    elif call.data == 'delete2':
      with open('man.txt', 'w') as f:
        f.write('')
      bot.send_message(call.message.chat.id, "List 2 deleted 📜")

print('Done 🫦')
bot.infinity_polling()
