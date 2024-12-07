from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def summon_browser():
    options = Options()
    options.add_experimental_option("detach", True)  # 手動操作のためブラウザを閉じない
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

if __name__ == "__main__":
    driver = summon_browser()
    driver.get("https://3icecream.com/login?from=logout")
    input("ログインが完了したらEnterを押してください...")
    driver.quit()