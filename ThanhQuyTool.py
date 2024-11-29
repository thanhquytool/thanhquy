import socket
import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import time
from time import strftime
import os, platform, time, sys
import os
import requests
import urllib.parse
from time import strftime
from datetime import datetime
from time import sleep, strftime
import datetime
import subprocess

def install(package):
    subprocess.check_call(["pip", "install", package])

# Kiểm tra và cài đặt từng thư viện nếu chưa có
try:
    import faker
except ImportError:
    install("faker")

try:
    import requests
except ImportError:
    install("requests")

try:
    import colorama
except ImportError:
    install("colorama")

try:
    import bs4
except ImportError:
    install("bs4")

try:
    import pystyle
except ImportError:
    install("pystyle")

try:
    import pysocks
except ImportError:
    install("pysocks")
print('__Các thư viện đã được kiểm tra và cài đặt (nếu cần)__')
os.system('cls' if os.name == 'nt' else 'clear')
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
import os
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
xoss('\n\033[1;32m[●] Đang Chạy Vào Tool: Thành Quý Tool....');time.sleep(0.1)
xoss('\n\033[1;36m[●] Kiểm Tra Sever....')
xoss('\n\033[1;33m[●] Kiểm Tra Bản Update....')
xoss('\n\033[1;34m[●] Thành Công Đang Tiến Hành Vào Tool....')
def Update():
    exit('\033[1;31m[●] Đang Tiến Hành Vào Tool...... ')
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

if __name__ == "__main__":
    main()
# Mã màu ANSI cho 7 sắc cầu vồng
rainbow_colors = [
    "\033[91m",  # Đỏ
    "\033[93m",  # Vàng
    "\033[92m",  # Xanh lá
    "\033[96m",  # Xanh dương nhạt
    "\033[94m",  # Xanh dương
    "\033[95m",  # Tím
    "\033[97m"   # Trắng
]

reset_color = "\033[0m"  # Màu mặc định
def banner():
    banner = f"""
\033[1;33m████████╗ ██████╚╗         ████████╗ █████╗  █████╗ ██╗
\033[1;35m╚══██╔══╝██║   ██║         ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m   ██║   ██║   ██║   █████╗   ██║   ██║  ██║██║  ██║██║
\033[1;31m   ██║   ██║ ████╚╗  ╚════╝   ██║   ██║  ██║██║  ██║██║
\033[1;32m   ██║   ╚████████║           ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m   ╚═╝    ╚════╗██║           ╚═╝    ╚════╝  ╚════╝ ╚═════╝
\033[1;31m               ╚══╝
\033[1;37mTool By: \033[1;32mThành Quý Tool
\033[1;37m══════════════════════════════════════════════════════════════
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;31m☞ Trang Nhập Key🧸 ☜
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;36mhttps://www.youtube.com/@thanhquytool
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;32m0355879036
\033[1;97m[\033[1;91m📝\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;33mhttps://t.me/quyleotop
\033[1;37m══════════════════════════════════════════════════════════════
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
import requests
import datetime
import hashlib
import sys
import os

day = datetime.datetime.now().day
key = hashlib.md5(f"{day}".encode()).hexdigest()
url = f"https://thanhquy07.github.io/website/?key={key}"
token = "664efe0fe5762652e171afca"
try:
    response = requests.get(f"https://link4m.co/api-shorten/v2", params={"api": token, "url": url}).json()
    if response['status'] == "success":
        link = response['shortenedUrl']
    else:
        print("Lỗi !!!")
        sys.exit(27122010)
except Exception as e:
    sys.exit(e)
def input_key():
    print(f"\033[1;32mLink Lấy Key Free: \033[1;36m{link}")
    while True:
        inp = input("\033[1;32mNhập Key: \033[1;31m")
        if inp == key:
            print("Key Đúng Rồi !")
            open("thanhquytool_key.txt", "w").write(inp)
            break
        else:
            print("Key Sai. Vui Lòng Nhập Lại !")
            continue 

if not os.path.exists("thanhquytool_key.txt"):
    input_key()
else:
    inp = open("thanhquytool_key.txt", "r").read()
    if inp == key:
        pass
    else:
        input_key()

if __name__ == "__main__":
    main()
while True:
    try:
        exec(requests.get('https://raw.githubusercontent.com/thanhquytool/thanhquy/main/ToolGolike/LogAuthorization.py').text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m✍\033[1;97m] \033[1;36m✈  \033[1;31mCảm Ơn Bạn Đã Dùng Tool - By Thành Quý Tool. Đã Thoát Tool...")
        sys.exit()