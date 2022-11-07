from http.client import responses
import requests
from pprint import pprint

sheety_spi_endpoint = "https://api.sheety.co/d1a4e410582ffd5f39a3f28dbc84ac15/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_sheet_details(self):
        responses = requests.get(url=sheety_spi_endpoint)
        responses.raise_for_status()
        self.destination_data = responses.json()
        return self.destination_data["prices"]

    def destination_code_update(self):
        for city in self.destination_data:
            parameter = {
                "price" : {
                    "iataCode" : city["iataCode"]
                }
            }

            responses = requests.put(url=f"{sheety_spi_endpoint}/{city['id']}", json=parameter)
            print(responses.text)

