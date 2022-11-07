# list = []
# with open("weather_data.csv") as data:
#     list = data.readlines()
#     print(list)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # for row in data:
#     #     print(row)

#     #extracting temprature from data
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)

   
#pandas library
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

#to extract temp
temp = data["temp"]
print(temp)         #3 lines vs 8 lines using pandas