import requests
import sys

while True:
    try:
        exec(requests.get('https://raw.githubusercontent.com/thanhquytool/thanhquy/main/ThanhQuyTool.py').text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m✍\033[1;97m] \033[1;36m✈  \033[1;31mCảm Ơn Bạn Đã Dùng Tool - By Thành Quý Tool. Đã Thoát Tool...")
        sys.exit()