import pandas as pd

# Read the CSV file using pandas
data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

# Filter the data to find the length of the gray squirrels
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

# Print the filtered data
print(gray_squirrels)

