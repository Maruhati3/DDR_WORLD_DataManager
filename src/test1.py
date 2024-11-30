from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

login_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/login.html'

# OpenAIのウェブサイトにアクセス
driver.get(login_url)

home_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/top/index.html'

# input("test...")
try:
    print(f"待機中... {home_url} に遷移するまで待ちます。")
    
    # URLが遷移するのを監視
    while True:
        current_url = driver.current_url  # 現在のURLを取得
        
        if current_url == home_url:
            print(f"URL '{home_url}' に遷移しました！次の処理を実行します。")
            break  # 遷移したらループを抜ける
        
        # 一定時間待機してから再チェック
        time.sleep(2)
    
    # ここから、遷移後に実行したい処理を行う
    print("遷移後の処理を開始します。")


    while True:
        # name_strクラスのタグを取得
        status_element = driver.find_element(By.CLASS_NAME, "name_str")  # idは適宜変更
        
        # タグの内容が "true" かどうか確認
        if status_element.text.lower() != "---":
            print("user name: "+status_element.text.lower())
            # ここで後の処理を実行
            break
        
        # 一定時間待機してから再チェック
        time.sleep(1)

except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    # 後の処理が終わったらブラウザを閉じる
    # Seleniumからクッキーを取得
    cookies = driver.get_cookies()
    # print("Seleniumで取得したクッキー:", selenium_cookies)

# Requestsのセッションを作成
# session = requests.Session()

driver.quit()

# Requestsでデータを操作
target_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/flare_data_single.html'

# response = session.get(target_url)
# print("取得したデータ:")
# print(response.text)

options.add_argument("--headless")
driver2 = webdriver.Chrome(options=options)

driver2.get(home_url)

# Seleniumから取得したクッキーをRequestsのセッションにセット
for cookie in cookies:
    cookie_dict = {
            'name': cookie['name'],
            'value': cookie['value']
        }
    driver2.add_cookie(cookie_dict)

driver2.get(target_url)

tables = driver2.find_elements(By.ID, "data_tbl")
titles = driver2.find_elements(By.CLASS_NAME, "graph_title")
# print(tables.text)

# contents = driver2.page_source
with open("row_output.txt", "w", encoding="utf-8") as flare_file:
    for title, table in zip(titles, tables):
        flare_file.write(title.text+"\n")
        flare_file.write(table.text+"\n")
        flare_file.write("-" * 20+"\n")

driver2.quit()