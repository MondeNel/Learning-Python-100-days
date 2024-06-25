# import csv

# # Open the CSV file
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
    
#     # Initialize an empty list to store temperatures
#     temperatures = []
    
#     # Skip the header row
#     next(data)
    
#     # Iterate through each row in the CSV file
#     for data_row in data:
#         # Extract the temperature value and convert it to an integer
#         temp = int(data_row[1])
        
#         # Append the integer temperature to the temperatures list
#         temperatures.append(temp)
    
#     # Print the list of temperatures
#     print(temperatures)


import pandas as pd

# Read the CSV file using pandas
data = pd.read_csv("weather_data.csv")

# print out the data in a table format
print(data)

# Extract the temperatures and convert them to a list of integers
temperatures = data["temp"].tolist()

# Print the list of temperatures
print(temperatures)
