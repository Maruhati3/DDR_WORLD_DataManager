from selenium import webdriver
import requests
import time
options = webdriver.ChromeOptions()

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

# OpenAIのウェブサイトにアクセス
driver.get('https://p.eagate.573.jp/game/ddr/ddrworld/login.html')
# 目標のウェブサイトを設定
target_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/top/index.html'

try:
    print("目標のURLに移動するまで待機中")
    while True:
        current_url = driver.current_url
        #print(f"現在のURL: {current_url}")  # デバッグ用
        if current_url == target_url:
            print("目標URLに移動しました。")
            break
        time.sleep(2)  # 1秒ごとにチェック
finally:
    
    
    # Seleniumからクッキーを取得
    selenium_cookies = driver.get_cookies()
    print("Seleniumで取得したクッキー:", selenium_cookies)

# Requestsのセッションを作成
session = requests.Session()

# Seleniumから取得したクッキーをRequestsのセッションにセット
for cookie in selenium_cookies:
    session.cookies.set(cookie['name'], cookie['value'])

# Requestsでデータを操作
target_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/top/index.html'

response = session.get(target_url)
print("取得したデータ:")
print(response.text)

# ブラウザを終了
driver.quit()




input("test...")

