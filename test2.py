import os
from selenium import webdriver


def test_driver():
    chrome_driver = os.path.join('chromedriver')

    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    driver.implicitly_wait(3)
    driver.quit()

    assert driver is not None
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_driver = os.path.join('chromedriver')

wd = driver = webdriver.Chrome(chrome_driver, options=chrome_options)
wd.get("http://www.naver.com")
wd.get_screenshot_as_file("TEST.png")
