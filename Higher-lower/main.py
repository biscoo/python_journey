import art
import random
import game_data

# Load data and assets
data_list = game_data.data
logo = art.logo
vs = art.vs

print(logo)

# Copy the data so we can safely remove items without affecting the original
available_choices = data_list.copy()

# Get initial random pair
random_choice = random.sample(available_choices, 2)

# Remove them from the available list to avoid repetition
for item in random_choice:
    available_choices.remove(item)

life = 5
win = True

# Game loop
while life and len(available_choices) > 0:
    # Display comparison
    print(f"Compare A: {random_choice[0]['name']}, a {random_choice[0]['description']}, from {random_choice[0]['country']}")
    print(vs)
    print(f"Compare B: {random_choice[1]['name']}, a {random_choice[1]['description']}, from {random_choice[1]['country']}")

    # Get user choice
    choice = input("Who has more followers? 'A' or 'B': ").lower()
    print(logo)

    # Check which choice is correct
    a_followers = random_choice[0]['follower_count']
    b_followers = random_choice[1]['follower_count']

    if choice == 'a' and a_followers > b_followers:
        print("✅ Correct!")
        # Keep A, replace B
        if available_choices:
            new_sample = random.sample(available_choices, 1)[0]
            available_choices.remove(new_sample)
            random_choice[1] = new_sample

    elif choice == 'b' and b_followers > a_followers:
        print("✅ Correct!")
        # Keep B, replace A
        if available_choices:
            new_sample = random.sample(available_choices, 1)[0]
            available_choices.remove(new_sample)
            random_choice[0] = new_sample

    else:
        life -= 1
        print(f"❌ Wrong Answer! You have {life} lives remaining.\n")

# Game over
print("💀 You lost! Try again.")
