# Read the letter template
with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter_lines = file.readlines()

# Read invited names
with open("./Input/Names/invited_names.txt", "r") as file:
    names_list = file.readlines()

# Create personalized letters
for name in names_list:
    invite_name = name.strip()

    # Create a copy of the template for each person
    new_letter_lines = letter_lines.copy()
    new_letter_lines[0] = f"Dear {invite_name},\n"

    # Combine all lines into one string
    final_letter = "".join(new_letter_lines)

    # Write the personalized letter to a file
    with open(f"./Output/ReadyToSend/{invite_name}.txt", "w") as file:
        file.write(final_letter)
