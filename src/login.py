from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

def login():
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
        cookie_file_name = "cookie.pkl"
        cookies = driver.get_cookies()
        with open(cookie_file_name, 'wb') as cookie_file:
            # cookie_file.write(driver.get_cookies())
            pickle.dump(cookies, cookie_file)
        # print("Seleniumで取得したクッキー:", selenium_cookies)

    # Requestsのセッションを作成
    # session = requests.Session()

    driver.quit()

if __name__ == "__main__":
    login()