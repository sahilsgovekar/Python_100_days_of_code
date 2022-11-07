from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

twitter_login_email = "techbro1947@gmail.com"
twitter_login_pass = "Techbro@1947"
twitter_username = "Techbro1947"
twitter_url = "https://twitter.com/compose/tweet"
speedtest_website = "https://www.speedtest.net/"

chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.serv = Service(chrome_driver)
        self.driver = webdriver.Chrome(service=self.serv)
        self.garent_upload = 50
        self.garent_download = 50

    def get_internet_speed(self):
        self.driver.get(url=speedtest_website)
        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        time.sleep(10)
        start.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span").text
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span").text
        print(f"Download Speed : {download_speed} \n Upload_Speed : {upload_speed}")
        time.sleep(3)
        self.driver.close()
        if download_speed < self.garent_download and upload_speed < self.garent_upload:
            self.tweet_at_provider(f"Download speed is {download_speed} and upload speed is {upload_speed} noas promised")


    def tweet_at_provider(self, message):
        self.driver.get(url=twitter_url)
        time.sleep(10)
        user = self.driver.find_element("name", "text")
        user.send_keys(twitter_login_email)
        email_next = self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div")
        email_next.click()
        time.sleep(5)
        user = self.driver.find_element("name", "password")
        user.send_keys(twitter_login_pass)
        login = self.driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div")
        login.click()
        time.sleep(3)
        twee = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div")
        twee.send_keys()
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click(message)


object = InternetSpeedTwitterBot()
object.get_internet_speed()
# object.tweet_at_provider()
