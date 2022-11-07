import pandas
data = pandas.read_csv("squreldata.csv")
fur_gray = len(data[data["Primary Fur Color"] == "Gray"])
fur_black = len(data[data["Primary Fur Color"] == "Black"])
fur_c = len(data[data["Primary Fur Color"] == "Cinnamon"])

dict = {
    "color" : ["Gray", "Black", "Cinemon"],
    "numbers" : [fur_gray, fur_black, fur_c]
}

count_data = pandas.DataFrame(dict)
print(count_data)
count_data.to_csv("count_data.csv")