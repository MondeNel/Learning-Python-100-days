import pandas as pd

# Read the CSV file using pandas
data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

# Filter the data to find the length of the squirrels
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

#Create a Dictionary of the data
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels, red_squirrels, black_squirrels]
}

#Convert into a DataFrame
data_squirrels = pd.DataFrame(data_dict)

# Print the data frame
print(data_squirrels)

#Convert to CSV file
data_squirrels.to_csv("squirrel_count.csv")