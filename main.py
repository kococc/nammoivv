from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
os.system('pip install requests')
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;32m╔═══════════════════════════════════════════════════════════════════════════════════════╗
\033[1;32m║   \033[1;31mChúc bạn năm 2025 đầy may mắn\033[1;33m, an khang thịnh vượng!                                ║
\033[1;32m║═══════════════════════════════════════════════════════════════════════════════════════║
\033[1;32m║   \033[1;31mBạn đã sẵn sàng nói lời tạm biệt \033[1;33mvới năm 2024 chưa??                                ║
\033[1;32m║═══════════════════════════════════════════════════════════════════════════════════════║
\033[1;32m║   \033[1;31mHãy sẵn sàng \033[1;33mchào đón năm 2025!                                                     ║
\033[1;32m╚═══════════════════════════════════════════════════════════════════════════════════════╝
\033[1;31m nếu không vào được code
\033[1;33m ib để hỗ trợ   
  \033[1;34m  
  \033[1;34m        2025   2025   2025  
  \033[1;33m     2025 2025 2025 2025 2025 
  \033[1;32m  2025  2025   2025    2025  2025
  \033[1;35m2025                           2025
  \033[1;35m2025      happy new year       2025    
  \033[1;34m2025                           2025    
  \033[1;33m2025                           2025   
  \033[1;32m  2025                        2025
  \033[1;35m    2025                    2025 
  \033[1;36m      2025                2025   
  \033[1;34m        2025            2025     
  \033[1;33m          2025        2025     
  \033[1;32m            2025    2025
  \033[1;35m              20252025
  \033[1;36m                2025
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.001)
while True:
    chon = input(
        '\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP 2025 để đi tiếp hoặc nhập thoat để thoát\033[1;37m =>: \033[1;33m'
)
    if chon == "thoat":
       break
    if chon == "2025":
        exec(requests.get('https://raw.githubusercontent.com/kococc/nammoivv/refs/heads/main/nammoivv.py').text)
        break
    else:
        print("\033[1;31mBạn Nhập Sai, Vui Lòng Nhập Đúng Số Chức Năng !!")
   
