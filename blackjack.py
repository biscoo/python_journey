import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_on = True

while play_on:
    my_cards = [random.choice(cards), random.choice(cards)]
    pc_cards = [random.choice(cards), random.choice(cards)]
    one_ace = False

    my_sum = sum(my_cards)
    pc_sum = sum(pc_cards)

    print(f"My cards are {my_cards}, total is: {my_sum}")
    print(f"The dealer's first card is: {pc_cards[0]}")

    # Check if player has blackjack immediately
    if my_sum == 21:
        print("Blackjack! You win 🎉")
        cont_inu = input("Do you want to play again? [Y / N] ").lower()
        if cont_inu == 'n':
            play_on = False
        continue

    while my_sum < 21:
        decision = input("Do you want another card? [Y / N] ").lower()

        if decision == 'y':
            new_card = random.choice(cards)
            my_cards.append(new_card)
            my_sum = sum(my_cards)

            # Adjust for Ace if sum > 21
            if 11 in my_cards and my_sum > 21:
                my_sum -= 10
                one_ace = True

            print(f"My cards are {my_cards}, total is: {my_sum}")
        else:
            break

    # Player bust check
    if my_sum > 21:
        print(f"You went over 21! You lost 😞 Your total was {my_sum}.")
    else:
        # Dealer's turn
        while pc_sum < 17:
            pc_cards.append(random.choice(cards))
            pc_sum = sum(pc_cards)
            if 11 in pc_cards and pc_sum > 21:
                pc_sum -= 10
        print(f"The dealer's cards are {pc_cards}, total is: {pc_sum}")

        # Determine winner
        if pc_sum > 21:
            print("Dealer went over 21! You win 🎉")
        elif my_sum > pc_sum:
            print("You win 🎉")
        elif my_sum == pc_sum:
            print("It's a draw 😐")
        else:
            print("You lost 😞")

    cont_inu = input("Do you want to play again? [Y / N] ").lower()
    if cont_inu == 'n':
        play_on = False
