import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_driver = os.path.join('chromedriver')

driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.get("http://ncov.mohw.go.kr/bdBoardList_Real.do")
driver.get_screenshot_as_file("TEST1.png")
element = driver.find_element_by_class_name("c_chart c_chart_pt")
element_png = element.screenshot_as_png
with open('ttt.png', "wb") as file:
  file.write(element_png)

driver.quit()
