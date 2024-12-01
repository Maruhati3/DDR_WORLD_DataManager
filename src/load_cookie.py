import pickle
import os
import requests
from login import login

# 1. .pklファイルからCookieを読み込む
def load_cookies(cookie_file):
    if not os.path.exists(cookie_file):
        # cookie.pkl が存在しない場合、-1 を返す
        print("cookie.pkl not exists\n")
        return -1
    
    else: 
        with open(cookie_file, 'rb') as f:
            cookies = pickle.load(f)
        return cookies

# 2. Cookieを使って指定URLにアクセス
def get_page_with_cookies(cookie_file):
    # requestsにCookieをセット

    # クッキーをロード
    cookies = load_cookies(cookie_file)

    if cookies == -1:
        login()
        cookies = load_cookies(cookie_file)

    session = requests.Session()
    # session.cookies.update(cookies)

    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    return session
