from http.client import responses
import requests

user_sheety_api_endpoint = "https://api.sheety.co/d1a4e410582ffd5f39a3f28dbc84ac15/flightDeals/users"


print("Welcome to Flight Club \nWe will find best flight deals and email you")

first_name = input("Enter your first name : ")
last_name = input("Enter your Last name : ")
email = input("Enter your Email : ")
re_email = input("Re-enter your email to confirm : ")
if email == re_email:
    entry = True
    print(f"Hey {first_name}, Enterd email and re-enterd email does'nt match")

if entry:
    try:
        parameter = {
            "user" : {
                "firstName" : first_name,
                "lastName" : last_name,
                "email" : email
            }
        }

        responses = requests.post(url=user_sheety_api_endpoint, json=parameter)
        print(f"Hey {first_name}, You'r into the Flight Club")
    
    except:
        print(print(f"Hey {first_name}, problem with the server, Try again later"))
