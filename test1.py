from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth

service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# create a ChromeOptions object
options = webdriver.ChromeOptions()

#run in headless mode
#options.add_argument("--headless")

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')

# disable pop-up blocking
#options.add_argument('--disable-popup-blocking')

# start the browser window in maximized mode
#options.add_argument('--start-maximized')

# disable extensions
#options.add_argument('--disable-extensions')

# disable sandbox mode
#options.add_argument('--no-sandbox')

# disable shared memory usage
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=service, options=options)


# OpenAIのウェブサイトにアクセス
driver.get('https://p.eagate.573.jp/game/ddr/ddrworld/login.html')
# driver.get('https://www.google.com')

input("test...")