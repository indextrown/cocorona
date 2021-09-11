from selenium import webdriver
from time import sleep

url = "http://www.naver.com" 

# chromedriver 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')               # headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')               # headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
driver.get(url)

# adding the loading time.
sleep(0.1)

# chapture!
driver.save_screenshot("screenshot.png")

# 브라우저를 닫는다.
driver.close()



