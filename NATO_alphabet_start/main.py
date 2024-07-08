student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

# Load the CSV file into a DataFrame
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create the dictionary using dictionary comprehension
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Step 2: Function to generate phonetic code words from user input
def generate_phonetic():
    word = input("Enter a word: ").upper()  # Convert input to uppercase to match dictionary keys
    phonetic_code_words = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]
    print(phonetic_code_words)

# Call the function to generate and print phonetic code words
generate_phonetic()