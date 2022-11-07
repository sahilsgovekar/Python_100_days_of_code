from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"

ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

driver.get(url)
count = driver.find_element("id", "articlecount")

# count.click()

print(count.text.split(" ")[0])


driver.close()



