from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome('chromedriver', options=chrome_options)

wd.get("http://www.naver.com")

wd.get_screenshot_as_file("TEST.png")

from google.colab import files
files.download("TEST.png")
