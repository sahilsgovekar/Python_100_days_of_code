##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

my_email = "techbro1947@gmail.com"
passward = "fndhamqwszfjzyqf"

# 1. Update the birthdays.csv
birth_data = pandas.read_csv("birthdays.csv")
birth_record = birth_data.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_date = today.day
today_month = today.month
for i in birth_record:
    if i["month"] == today_month and i["day"] == today_date:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        r = random.randint(1, 3)
        with open(f"letter_templates/letter_{r}.txt") as lett:
            letter = lett.read()
        letter = letter.replace("[NAME]", i["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        # with smtplib.SMTP("smpt.gmail.com", port=587) as connection:
        #     print("2")
        #     connection.starttls()
        #     print("3")
        #     connection.login(user=my_email, password=passward)
        #     print("4")
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs=email_rec,
        #         msg=f"Subject:Happy Birthday Dear \n\n {letter}"
        #     )
        with  smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passward)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=i["email"], 
                msg=f"Subject:Happy Birthday Dear \n\n {letter}"
                )









