from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://www.linkedin.com/my-items/saved-jobs/"
chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"
email = "techbro1947@gmail.com"
passw = "Techbro@1947"


serv = Service(chrome_driver)

driver = webdriver.Chrome(service=serv)

driver.get(url)


login = driver.find_element(By.CLASS_NAME, "main__sign-in-link")
login.click()
time.sleep(5)
userid = driver.find_element("name", "session_key")
password = driver.find_element("name", "session_password")
userid.send_keys(email)
password.send_keys(passw)
loh_in = driver.find_element(By.CLASS_NAME, "btn__primary--large")
loh_in.click()
time.sleep(5)

'''
    Code was fixed but yet to update
'''


# driver.close()

