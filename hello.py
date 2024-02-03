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
    bot.send_video(message.chat.id,h, caption="""𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒃𝒐𝒕 𝒃𝒚 : @i_7rR"""),parse_mode='html',reply_markup=mss)
@bot.callback_query_handler(func=lambda call:True)
def qwere(call):
    if call.data =='mos':
        li(call.message)
def li(message):
    error=0
    done=0
    
    while True:
    	AB ='qwertyuiopasdfghjklzxcvbnm'
                num = '1234567890'
                f = '_.'
    	aa = str("".join(random.choice(AB) for i in range(1)))
    	bb = str("".join(random.choice(AB) for i in range(1)))
                dd = str("".join(random.choice(num) for i in range(1)))
                abd = str("".join(random.choice(f) for i in range(1)))
                c1 = (aa + bb + aa + abd + aa)
                c2 = (aa + aa + aa + abd + bb)
                c3 = (aa + dd + aa + dd + aa)
                c4 = (aa + aa + abd + aa + aa)
                c5 = (bb + bb + bb + aa + aa)
                c6 = (aa + dd + dd + aa + dd)
                c7 = (aa + abd + aa + abd + dd)
                c8 = (dd + abd + dd + abd + aa)
                c9 = (bb + dd + bb + abd + bb)
                c10 = (abd + abd + aa + aa + abd)
                c11 = (bb + bb + dd + dd + dd)
                c12 = (aa + aa + aa + abd + aa)
                c13 = (aa + abd + dd + dd + dd)
                c14 = (aa + aa + dd + dd + dd)
                user = (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14)
                
    	req = requests.get(f'https://t.me/{user}').text
    	if '"robots"' in req:
    	       done+=1
    	       bot.send_message(message.chat.id,f"""Hit User Tele
•----------------------------------------•
Username - ( @{user} )
•----------------------------------------•
@GG8MG""",parse_mode="html")
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