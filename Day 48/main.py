from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"
serv = Service(chrome_driver)
driver = webdriver.Chrome(service=serv)
driver.get("https://www.python.org/")

driver.close()
driver.quit()