import requests

parameter = {
    "lat" : 12.9716,
    "lon" : 77.580643,
    "exclude" :"current,minutely,daily",
    "appid" : "6553de24eec2f3b09c80938b8965ab9b"

}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
data = response.json()
for i in range(0, 12):
    condition_code = int(data["hourly"][i]["weather"][0]["id"])
    if condition_code < 700:
        print(i, condition_code)
        print("Bring an umbrella")
        break

#implementation of trilio ----