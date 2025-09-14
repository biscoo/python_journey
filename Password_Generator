import random  # Import random module for generating random samples

# ------------------------------
# Character sets for password
# ------------------------------
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ------------------------------
# User input
# ------------------------------
print("Welcome to the PyPassword Generator!")

# Ask user how many letters, symbols, and numbers they want in the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# ------------------------------
# Password generation
# ------------------------------
password = []

# Add random letters
password = password + random.sample(letters, nr_letters)

# Add random numbers
password = password + random.sample(numbers, nr_numbers)

# Add random symbols
password = password + random.sample(symbols, nr_symbols)

# Join the characters into a single string
my_password = ''.join(password)

# ------------------------------
# Output
# ------------------------------
print(f'Your Password is: {my_password}')
