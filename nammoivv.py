import time
from colorama import Fore, init
import random

# Khởi tạo Colorama
init(autoreset=True)

# Danh sách các màu có sẵn trong colorama
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# Hàm để viết chữ theo thời gian với nhiều màu sắc
def write_text_slowly_multicolor(text, delay=0.1):
    for char in text:
        # Chọn màu ngẫu nhiên cho từng ký tự
        color = random.choice(colors)
        print(color + char, end='', flush=True)  # In ra chữ với màu
        time.sleep(delay)  # Dừng một khoảng thời gian giữa các ký tự

# Ví dụ sử dụng hàm trên
text = "NĂM MỚI ZUI ZẺ NHA=)"
print("code made by python")
write_text_slowly_multicolor(text, 0.1)
