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
data = pd.read_csv("weather_data.csv") # The whole table is a DATAFRAME

# Extract the temperatures and convert them to a list of integers
temperatures = data["temp"] # day, temp, condition are SERIES

# Calculate the average temperature
average_temperature = temperatures.mean()

#Calculate the maximum temperature
max_temperature = temperatures.max()


# Print the average temperature
print(f"The average temperature is {average_temperature:.2f}°C")

# Print the maximum temperature
print(f"The maximum temperature is {max_temperature}°C")


#Convert Data to a Dictionary
data_dict = data.to_dict()





# Create a DataFrame from scratch
data_dict_students = {
    "student": ["Amy", "James", "Siya"],
    "grades": [89, 77, 50]
}

data_students = pd.DataFrame(data_dict_students)

# Convert to a CSV file
data_students.to_csv("students_data.csv", index=False)

# Print the table of students with grades
print(data_students)

# Extract the grades
grades = data_students["grades"]

# Extract the student names
student_names = data_students["student"]

# Calculate the highest grade
highest_grade = grades.max()

# Find the student with the highest grade
highest_grade_student = data_students[data_students["grades"] == highest_grade]["student"].iloc[0]

# Print the highest grade and the corresponding student
print(f"The highest grade is {highest_grade}% and it was obtained by {highest_grade_student}")