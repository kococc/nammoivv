import time
from time import sleep
from colorama import Fore, Style, init
import random

# Khởi tạo Colorama
init(autoreset=True)

# Danh sách các màu đậm và sáng hơn từ colorama
colors = [
    Style.BRIGHT + Fore.RED,       # Đỏ đậm
    Style.BRIGHT + Fore.GREEN,     # Xanh lá đậm
    Style.BRIGHT + Fore.YELLOW,    # Vàng đậm
    Style.BRIGHT + Fore.BLUE,      # Xanh dương đậm
    Style.BRIGHT + Fore.MAGENTA,   # Tím đậm
    Style.BRIGHT + Fore.CYAN,      # Xanh dương nhạt đậm
    Style.BRIGHT + Fore.WHITE,     # Trắng đậm
]

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

# Hàm để in banner với nhiều màu sắc ngẫu nhiên cho từng ký tự
def print_multicolor_banner():
    banner = """
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
print("Chúc mọi người năm mới vui vẻ nha")
