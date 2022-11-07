from urllib import response
import requests
from datetime import datetime

USERNAME = "techbro1947"
TOKEN = "abacad1947"
ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "abacad1947",
    "username" : "techbro1947",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
} 

# responses = requests.post(url=pixela_endpoint, json=user_params)
# print(responses.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Reading",
    "unit" : "hr",
    "type" : "float",
    "color" : "momiji"
}

header = {
    "X-USER-TOKEN" : TOKEN
}

# responses = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(responses.text)

pixel_post_endpoint = f"{graph_endpoint}/{ID}"

today = datetime.now()

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5.45"
}

# responses = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=header)
# print(responses.text)


delete_pixel_api = f"{pixel_post_endpoint}/{today.strftime('%Y%m%d')}"

responses = requests.delete(url=delete_pixel_api, headers=header)
print(responses.text)