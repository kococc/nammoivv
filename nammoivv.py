import sleep
from colorama import Fore, init
import random

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
text = "HÁP PY NIU DIA=)"
print("code made by python")
write_text_slowly_multicolor(text, 0.1)
init(autoreset=True)

# Danh sách các màu có sẵn trong colorama
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# Hàm để in banner với nhiều màu sắc ngẫu nhiên cho từng ký tự
def print_multicolor_banner():
    banner="""
           2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025
                                    2025  2025                     2025                           2025  2025
                                    2025  2025                     2025                           2025  2025
                                    2025  2025                     2025                           2025  2025
                                    2025  2025                     2025                           2025  2025
                                    2025  2025                     2025                           2025  2025
                                    2025  2025                     2025                           2025  2025
           2025 2025 2025 2025 2025 2025  2025                     2025  2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025
           2025                           2025                     2025  2025                                                    2025           2025                           2025                     2025  2025                                                    2025
           2025                           2025                     2025  2025                                                    2025
           2025                           2025                     2025  2025                                                    2025
           2025                           2025                     2025  2025                                                    2025
           2025                           2025                     2025  2025                                                    2025 
           2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025  2025 2025 2025 2025 2025 2025
"""
    for line in banner.split('\n'):
        for char in line:
            # Chọn màu ngẫu nhiên cho mỗi ký tự
            color = random.choice(colors)
            print(color + char, end='', flush=True)
        print()  # In một dòng mới sau mỗi dòng banner

# Gọi hàm để in banner nhiều màu sắc
print_multicolor_banner()
print("chúc mọi người năm mới vui vẻ nha")
