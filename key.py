import base64
import requests
import hashlib
import socket
import random
from colorama import Fore, Style, init

# Khởi tạo colorama
init(autoreset=True)

# Danh sách các màu đậm
COLORS = [
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.GREEN,
    Style.BRIGHT + Fore.YELLOW,
    Style.BRIGHT + Fore.BLUE,
    Style.BRIGHT + Fore.MAGENTA,
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.WHITE,
]

def get_random_color():
    """Trả về một màu ngẫu nhiên (đậm)."""
    return random.choice(COLORS)

def create_key_from_ip(ip_address):
    """
    Tạo key từ địa chỉ IP bằng cách băm SHA-256 và mã hóa Base64.
    """
    try:
        sha256_hash = hashlib.sha256(ip_address.encode()).digest()
        base64_key = base64.b64encode(sha256_hash).decode()
        return base64_key
    except Exception as e:
        return f"Error: {e}"

def validate_key(input_key, expected_key):
    """
    Xác thực key người dùng nhập với key đã mã hóa.
    """
    return input_key == expected_key

def main():
    # Lấy địa chỉ IP hiện tại
    ip_address = socket.gethostbyname(socket.gethostname())

    # Tạo key từ IP mạng
    generated_key = create_key_from_ip(ip_address)

    # Hiển thị thông tin với màu sắc ngẫu nhiên (đậm)
    print(get_random_color() + f"Ip Của Bạn Là :{ip_address}")
    print(get_random_color() + "zalo 0943040079")
    print(get_random_color() + "ib chủ code để lấy key")
    print(get_random_color() + "key dùng vv chắc thế")
    print(get_random_color() + "key đổi theo ip mạng và đã được enc")
    print(get_random_color() + "nếu không thấy ip thì lên web tìm ")

    # Lặp lại nhập key cho đến khi đúng
    while True:
        # Nhập key từ người dùng
        user_key = input(get_random_color() + "Nhập key để tiếp tục: ").strip()

        # Xác thực key
        if validate_key(user_key, generated_key):
            print(get_random_color() + "Key chính xác! Bạn có thể tiếp tục sử dụng code.")
            # Đặt code thực thi tại đây
            print(get_random_color() + "Chạy code của bạn...")
            break  # Thoát khỏi vòng lặp khi key đúng
        else:
            print(get_random_color() + "Key không hợp lệ. Truy cập bị từ chối. Nhập lại key.")

if __name__ == "__main__":
    main()

# Tiếp tục với mã khác
while True:
    chon = input(
        '\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP 1 ĐỂ VÀO CODE\033[1;37m =>: \033[1;33m'
    )

    if chon == "1":
        exec(requests.get('https://raw.githubusercontent.com/kococc/nammoivv/refs/heads/main/nammoivv.py').text)
        break
    else:
        print("\033[1;31mBạn Nhập Sai, Chọn Số 1 Để Vào Code!!")
