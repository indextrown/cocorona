import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_driver = os.path.join('chromedriver')

driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get("http://ncov.mohw.go.kr/")
driver.get_screenshot_as_file("TEST4.png")
element = driver.find_element_by_class_name("regional_patient_status_A")
element_png = element.screenshot_as_png
with open('TEST5.png', "wb") as file:
  file.write(element_png)

driver.quit()
