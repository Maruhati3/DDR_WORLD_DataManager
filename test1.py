from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=service, options=options)

# OpenAIのウェブサイトにアクセス
driver.get('https://p.eagate.573.jp/game/ddr/ddrworld/login.html')
# driver.get('https://www.google.com')

input("test...")