import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 12.972442 # Your latitude
MY_LONG = 77.580643 # Your longitude
my_email = "techbro1947@gmail.com"
passward = "fndhamqwszfjzyqf"

def in_my_range(lat, lon):
    if lat >= (MY_LAT-5) and lat <= (MY_LAT+5):
        if lon >= (MY_LONG-5) and lon <= (MY_LONG+5):
            return True


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(600)
    if in_my_range(iss_latitude, iss_longitude):
        if time_now <= sunrise or time_now >= sunset:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=passward)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs=my_email,
                    msg="iss is overhead"
                    )




