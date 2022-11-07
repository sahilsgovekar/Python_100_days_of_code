#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


data_manag = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manag.get_sheet_details()
pprint(sheet_data)

for i in sheet_data:
    if i["iataCode"] == '':
        i["iataCode"] = flight_search.code_search(i["city"])

data_manag.destination_data = sheet_data
# data_manag.destination_code_update()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        "BLR",
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight == None:
        pass

    elif flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

