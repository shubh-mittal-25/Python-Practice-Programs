import pandas

data = pandas.read_csv("2018_central_park_squirrel_census.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

gray_squirrels_count = len(gray_squirrels)
cinnamons_squirrels_count = len(cinnamon_squirrels)
black_squirrels_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamons_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("fur_color_squirrel_count.csv")
