import random
from hangman_words import word_list
from hangman_art import logo, stages

# Print game logo at the start
print(logo)

# Choose a random word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # <-- Debug: remove this in production if you don’t want to reveal the word

# Create a display with underscores for each letter
display = "_" * len(chosen_word)
display_list: list[str] = list(display)

# Set initial lives
lives: int = 6

print("Word to guess: " + display)

# Main game loop
while display != chosen_word:
    matched_word = display_list

    # Show remaining lives
    print(f'**************************** {lives} LIVES LEFT ****************************')

    guess = input("Guess a letter: ").lower()

    # Check if letter has already been guessed
    if guess in set(display_list):
        print("You already guessed that letter.")

    # Update display if guess is correct
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess and display_list[i] != guess:
            display_list[i] = guess

    # If guess is not in the word, lose a life
    if guess not in chosen_word and guess not in display_list:
        lives -= 1
        print(f"'{guess}' is not in this word.")

    # Check if lives run out
    if lives == 0:
        print(stages[lives])
        print("*********************** YOU LOSE ***********************")
        print("The correct word was: " + chosen_word)
        break

    # Update the current display
    display = "".join(matched_word)
    print(display)

    # Check if the player has won
    if display == chosen_word:
        print(stages[lives])
        print("**************************** YOU WIN ****************************")
        break

    # Show the current hangman stage
    print(stages[lives])
