import telebot
import os
from telebot import types
import requests
import random
token = input(' Enter Token : ')

bot = telebot.TeleBot(token)
ds = types.InlineKeyboardButton(text='Click HeaR To StarT',callback_data='mos')
me = types.InlineKeyboardButton(text='aBooD',url='https://t.me/i_7rR')
@bot.message_handler(commands=['start'])
def start(message):
    h = "https://telegra.ph/file/d5eb8964f7abc3c4fce1d.mp4"
    xz = message.from_user.first_name
    mss = types.InlineKeyboardMarkup()
    mss.row_width = 1
    mss.add(ds,me)
    bot.send_video(message.chat.id,h, caption='''𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒃𝒐𝒕 𝒃𝒚 : @i_7rR''',parse_mode='html',reply_markup=mss)
@bot.callback_query_handler(func=lambda call:True)
def qwere(call):
    if call.data =='mos':
        li(call.message)
def li(message):
    error=0
    done=0
    
    def username(client):
    AB = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    num = '1234567890'
    while True:
        mm = str("".join(random.choice(AB) for i in range(1)))
        nn = str("".join(random.choice(AB) for i in range(1)))
        ww = str("".join(random.choice(num) for i in range(1)))
        hh = str("".join(random.choice(AB) for i in range(1)))
        c = (mm + mm + mm + "_" + nn )
        c1 = (mm + "_" + nn + "_" + hh)
        c2 = (mm + "_" + mm + mm + ww)
        c3 = (mm + mm + mm + "_" + hh)
        c4 = (hh + "_" + mm + mm + mm)
        c5 = (nn  + mm + mm + "_" + mm)
        c6 = (mm + "_" + nn + nn + nn)
        c7 = (hh  + mm + ww + ww + ww)
        c8 = (mm + hh + ww + ww + ww)
        c9 = (mm + mm + ww + nn + nn)
        user = (c,c1,c2,c3,c4,c5,c6,c7,c8,c9)
        username = str("".join(random.choice(user)))
        check(client, username)
    	req = requests.get(f'https://t.me/{user}').text
    	if '"robots"' in req:
    	       done+=1
    	       bot.send_message(message.chat.id,f"""Hit User Tele
•----------------------------------------•
Username - ( @{user} )
•----------------------------------------•
@i_7rR""",parse_mode="html")
    	else:
    	       error+=1
    	       ws = types.InlineKeyboardMarkup(row_width=1)
    	       v1 = types.InlineKeyboardButton(f" DonE [{done}]",callback_data='mn')
    	       v2 = types.InlineKeyboardButton(f" BaD [{error}]",callback_data='mnm')
    	       Check = types.InlineKeyboardButton(f" ChecK [{user}]",callback_data='asnm')
    	       v3 = types.InlineKeyboardButton(f" Ptogrammer  ",url="https://t.me/i_7rR",callback_data='tynn')
    	       v4 = types.InlineKeyboardButton(f" Channel   ",url="https://t.me/l6303",callback_data='mnn')
    	       ws.add(v1,v2,v3,v4,Check)
    	       bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="(اهلا بك بدأ الصيد الان )",parse_mode='markdown',reply_markup=ws) 


bot.polling(True)