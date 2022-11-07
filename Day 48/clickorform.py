from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"

ser = Service(chrome_driver)
driver = webdriver.Chrome(service=ser)

# driver.get(url)
# search_box = driver.find_element("name", "search")
# search_box.send_keys("python")
# search_box.send_keys(Keys.ENTER)
# count.click()
# print(count.text.split(" ")[0])

url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url)
fname = driver.find_element("name", "fName")
lname = driver.find_element("name", "lName")
email = driver.find_element("name", "email")

fname.send_keys("Name")
lname.send_keys("lname")
email.send_keys("mail@gmail.com")

email.submit()
# submit = driver.find_element("class", "btn")
# submit.click()


# driver.close()



