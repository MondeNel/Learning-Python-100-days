
# with open("weather_data.csv") as data_file:
#     weather_data = data_file.readlines()
#     print(weather_data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for data_row in data:
        print(data_row)