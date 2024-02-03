import os
import sys
import random
import requests
import threading
tuks1 ='qwertyuioplkjhgfdsazxcvbnm'
R = '\033[1;32m'
G = '\033[1;31m'
E = '\033[1;33m'
K = '\033[1;39m'
F =('='*60)
H=(f"""{R}{F}
                   💤 7rR | عَبود
                @l6303
                                                         
{F}""")
print(H)
try:
	RUKS3 = int(input('عدد احرف الميل :'))
except:
	print('='*20)
	print(G+'راجاء وضع ارقام فقط')
	exit(0)
os.system('clear')
print(H)
RUKS_HED = {
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                        "Connection": "close",
                        "Host": "odc.officeapps.live.com",
                        "Accept-Encoding": "gzip, deflate",
                        "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                        "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                        "uaid": "d06e1498e7ed4def9078bd46883f187b",
                        "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"       
                        }
AS= 0
DS = 0                  
def ruks():
	global AS
	global DS		       	            	
	while True:			
		RuKs = str("".join(random.choice(tuks1)for i in range(RUKS3)))			
		j_n_q = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress="+RuKs+'@hotmail.com'+ "&_=1604288577990"
		RUKS_data = ''  		
		RUks = requests.get (j_n_q, data=RUKS_data, headers=RUKS_HED)
	
		if 'MSAccount' in RUks.text:
			AS+=1			
			print(f"""\r{E}Not Available: {G}{AS} {E}:Available: {R}{DS} {K};{RuKs}@hotmail.com""", end="")
			with open('Not Available.txt', 'a') as x:
				x.write(RuKs+'@hotmail.com'+ '\n')						
		else:	
			DS+=1
			print(f"""\r{E}Not Available: {G}{AS} {E}:Available: {R}{DS} {K};{RuKs}@hotmail.com""", end="")
			with open('Available.txt', 'a') as x:
				x.write(RuKs+'@hotmail.com'+ '\n')			
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join

         