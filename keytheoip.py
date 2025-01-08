import base64
import hashlib
import socket
import re

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

def is_valid_ip(ip):
    """
    Kiểm tra xem địa chỉ IP có hợp lệ không.
    """
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(ip) is not None

def main():
    while True:
        print("\n-------------------")
        print("Chọn một tùy chọn:")
        print("1. Sử dụng địa chỉ IP hiện tại")
        print("2. Nhập địa chỉ IP mạng mới")
        print("3. Thoát")
        print("-------------------")
        
        choice = input("Lựa chọn của bạn (1/2/3): ").strip()
        
        if choice == "1":
            ip_address = socket.gethostbyname(socket.gethostname())
            print(f"Địa chỉ IP hiện tại: {ip_address}")
            key = create_key_from_ip(ip_address)
            print(f"Key mã hóa từ IP mạng hiện tại: {key}")
        
        elif choice == "2":
            ip_address = input("Nhập địa chỉ IP mạng mới: ").strip()
            if is_valid_ip(ip_address):
                key = create_key_from_ip(ip_address)
                print(f"Key mã hóa từ IP mạng mới: {key}")
            else:
                print("Địa chỉ IP không hợp lệ. Vui lòng thử lại.")
        
        elif choice == "3":
            print("Thoát chương trình. Tạm biệt!")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
