from selenium import webdriver
from bs4 import BeautifulSoup
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
flare_url =  'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/flare_data_single.html'
status_url=  'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/index.html'

print('='*50)
response = session.get(target_url)
print("取得したデータtop:")
print(target_url)
print(response.url)
file=open('result.html','w')
file.write(str(BeautifulSoup(response.content,"html.parser")))
file.close()
print('='*50)


response= session.get(status_url)
print("取得したデータstatus:")
print(status_url)
print(response.url)
response= session.get(status_url)
file2=open('result2.html','w')
file2.write(str(BeautifulSoup(response.content,"html.parser")))
file2.close()

response= session.get(flare_url)
print("取得したデータflare:")
print(flare_url)
print(response.url)
response= session.get(flare_url)
file3=open('result3.html','w')
file3.write(str(BeautifulSoup(response.content,"html.parser")))
file3.close()


input('Enterでおわり')
# ブラウザを終了
driver.quit()




