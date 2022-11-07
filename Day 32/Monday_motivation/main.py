import datetime as dt
import smtplib
import random

my_email = "techbro1947@gmail.com"
passward = "fndhamqwszfjzyqf"

with open("quotes.txt") as data:
    data_read = data.read()
    datas = data_read.split("\n")

today = dt.datetime.now()
week_of_day = today.weekday()

if week_of_day == 3:
    with  smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passward)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="skillyourinovation@gmail.com", 
            msg=f"Subject:Monday Motivation \n\n{random.choice(datas)}"
            )