from urllib import response
import requests

age_api = gender_api = "https://api.genderize.io/?name="

name = input("name")

respons = requests.get(url=f"{age_api}{name}")
data = respons.json()["gender"]

print(data)


