import datetime
import time
import pyrogram
from pyrogram import Client
import requests
import os
from time import sleep
from pyrogram.errors import FloodWait, BadRequest
import re
import datetime
current_time = datetime.datetime.now().time()
hours = current_time.hour
minutes = current_time.minute
seconds = current_time.second
tok = input("EnTeR ToK :")
idown = 6330435571
qq = 0
ok = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=𝖿ᥙᥴ'𝗄 !')
app = Client("ACCC", api_id=13066983, api_hash="154e45eb588378308ad53f9bb8ed4bed",bot_token="6756691141:AAGwzBR4UwPYwt3YRYwgUjX7W5DBzE-3ga0")
with app:
 while True:
    username = set(filter(None, open("user.txt").read().split("\n")))
    for user in username:
        qq += 1
        print(qq)
        url = f"https://t.me/{user}"
        sleep(0.1)
        req = requests.get(url)
        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                op = requests.post(f'''https://api.telegram.org/bot{tok}/sendvideo?chat_id={idown}&video=https://t.me/aonrigh/187&caption=
𝗇𝖾𝗐 𝖿𝗅𝗈𝗈𝖽 𝗎𝗌𝖾𝗋 , 𝖺𝖻𝗈𝗈𝖽 𝗒𝖺𝖻'𝗁 🇮🇶 
এ〔 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 〕: 〔 @{user} 〕
এ〔 𝗍𝗂𝗆𝖾 〕: 〔 {hours}:{minutes}:{seconds} 〕
এ〔 𝖻𝗒 〕: @Prxey''')
                with open("user.txt", "r") as file:
                    lines = file.readlines()
                with open("user.txt", "w") as file:
                    for line in lines:
                     if user not in line:
                        file.write(line)
