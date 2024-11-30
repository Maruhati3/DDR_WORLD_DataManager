from selenium import webdriver

options = webdriver.ChromeOptions()

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

# OpenAIのウェブサイトにアクセス
driver.get('https://p.eagate.573.jp/game/ddr/ddrworld/login.html')

input("test...")