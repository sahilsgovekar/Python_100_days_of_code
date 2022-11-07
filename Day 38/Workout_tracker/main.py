import requests
import datetime
from requests.auth import HTTPBasicAuth



APP_ID = "29a6ba52"
API_KEY = "48e123e548b0149b9359bdd160ed0bff"

api_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

shety_api_endpoint = "https://api.sheety.co/d1a4e410582ffd5f39a3f28dbc84ac15/workoutTracking/workouts"

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "Content-Type" : "application/json"
}

input = input("Tell me which exercise you did : ")

parameter = {
    "query" : input,
    "gender" : "male",
    "weight_kg" : 62,
    "height_cm" : 182.88,
    "age" : 20
}

responses = requests.post(url=api_exercise_endpoint, json=parameter, headers=header)
responses.raise_for_status()
result = responses.json()

today_date = datetime.date.today().strftime("%d/%m/%y")
now_time = datetime.datetime.now().strftime("%X")

basic = HTTPBasicAuth('test', 'testshitty')

for data in result["exercises"]:
    parameter = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    responses = requests.post(url=shety_api_endpoint, json=parameter, auth=basic)
    print(responses.text)




