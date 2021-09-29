import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_driver = os.path.join('chromedriver')

driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get("https://www.jinju.go.kr/05190/05641.web")
body.find_element_by_class_name("btn_more").click()

driver.get_screenshot_as_file("TEST6.png")
element = driver.find_element_by_class_name("pr1")
element_png = element.screenshot_as_png
with open('TEST6.png', "wb") as file:
  file.write(element_png)

driver.quit()
