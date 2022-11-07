import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "techbro1947@gmail.com"
passward = "fndhamqwszfjzyqf"

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

responses = requests.get(url=URL, headers=header)

webdata = responses.content

# with open("htmldata.html", "w") as hd:
#     hd.write(webdata)

soup = BeautifulSoup(webdata, "lxml")
# print(soup.prettify())
price = soup.find(class_ = "a-price").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# #testing
# price_as_float = 78

if  price_as_float <= 100.00:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls
        connection.login(user=my_email, password=passward)
        connection.sendmail(
                        from_addr=my_email, 
                        to_addrs=my_email,
                        msg=f"current price is {price_as_float} below excepted"
        )