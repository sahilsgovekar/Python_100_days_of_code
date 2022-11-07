from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"

ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie = driver.find_element("id", "cookie")
while True:
    cookie.click()

