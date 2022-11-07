from email import message
import smtplib

my_email = "techbro1947@gmail.com"
passward = "fndhamqwszfjzyqf"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=passward)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="skillyourinovation@gmail.com", 
        msg="Subject:Hello \n\n Test")

