from selenium import webdriver
from time import sleep

url = "http://www.naver.com" 

# chromedriver 
driver = webdriver.Chrome("https://github.com/indextrown/testt/blob/main/chromedriver")
driver.get(url)

# adding the loading time.
sleep(0.1)

# chapture!
driver.save_screenshot("screenshot.png")

# 브라우저를 닫는다.
driver.close()



