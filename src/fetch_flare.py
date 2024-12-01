from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle
from flare_output import flare_to_csv

# Requestsでデータを操作
home_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/top/index.html'
target_url = 'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/flare_data_single.html'

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--headless")

driver2 = webdriver.Chrome(options=options)

driver2.get(home_url)

# Seleniumから取得したクッキーをRequestsのセッションにセット
cookie_file_name = "cookie.pkl"
with open(cookie_file_name, 'rb') as cookie_file:
    cookies = pickle.load(cookie_file)

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

out_file_name = "row_out_flare.txt"

# contents = driver2.page_source
with open(out_file_name, "w", encoding="utf-8") as out_file:
    for title, table in zip(titles, tables):
        out_file.write(title.text+"\n")
        out_file.write(table.text+"\n")
        out_file.write("-" * 20+"\n")

driver2.quit()

flare_to_csv(out_file_name)