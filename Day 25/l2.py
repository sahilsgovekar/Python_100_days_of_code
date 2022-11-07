import pandas
data = pandas.read_csv("weather_data.csv")

#challange: to compute average temperature from given data
# list = data["temp"].to_list()
# avg = sum(list) / len(list)
# print(f"Average temprature : {avg}")
# print(data["temp"].mean())
# #maximum value
# max_temp = data["temp"].max()


# #to pull out row ex-monday
# print(data[data.day == "Monday"])
# #to pull max temp row
# # print(data[data.temp == max_temp])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday.temp = (monday.temp * (9/5)) +32
# print(monday)

#creating data frame from scratch
dict = {
    "name" : ["mr x", "mr y"],
    "marks" : [99, 95]
}
data_marks =pandas.DataFrame(dict)
print(data_marks)
data_marks.to_csv("data_marks.csv")