from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"
username = "techbro1947"
password = "Techbro@1947"
url = "https://www.instagram.com/accounts/login/"

class Instafollowers:
    def __init__(self) -> None:
        self.serv = Service(chrome_driver)
        self.driver = webdriver.Chrome(service=self.serv)

    def login(self):
        self.driver.get(url)
        time.sleep(5)
        user_name = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
        user_name.send_keys(username)
        passw = self.driver.find_element("name", "password")
        passw.send_keys(password)
        login = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)")
        login.click()
        self.find_follower()



    def find_follower(self):
        time.sleep(10)
        ser = self.driver.find_element(By.CSS_SELECTOR, "#mount_0_0_V6 > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > section > nav > div._acc1._acc3 > div > div > div._aawf._aawg._aexm > input")
        ser.send_keys("virat kholi")
        time.sleep(3)
        ser.send_keys(Keys.ENTER)


    def follow(self):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#mount_0_0_GM > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > section > main > div > header > section > div.x1n2onr6.xeuugli.xs83m0k.x1q0g3np.x78zum5.x6s0dn4 > div._ab8w._ab94._ab99._ab9f._ab9k._ab9p._abb3._abcm > div > div:nth-child(3) > button").click()
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

obj = Instafollowers()
obj.login()