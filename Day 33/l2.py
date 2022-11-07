import requests

parameters = {
    "lat" : 12.972442,
    "lng" : 77.580643, 
    "formatted" : 0
}

responses = requests.get(url=" http://api.sunrise-sunset.org/json", params=parameters)
responses.raise_for_status()
data = responses.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)
