import pandas as pd

# Read the NATO phonetic alphabet CSV file
alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")

# Convert CSV data into a dictionary
# Format: {"A": "Alfa", "B": "Bravo", ...}
phonetic_dict = {row.letter: row.code for _, row in alphabet_data.iterrows()}

# Get user input
word = input("Enter a word or name: ").upper()

# Convert each letter to its NATO phonetic code
nato_code_words = [phonetic_dict[letter] for letter in word if letter.isalpha()]

print(nato_code_words)
