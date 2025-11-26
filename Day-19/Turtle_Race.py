from turtle import Turtle, Screen
import random

# Setup screen
screen = Screen()
screen.title("Turtle Race")

# Turtle configurations
turtle_data = {
    "purple": 50,
    "green": 0,
    "yellow": -50,
    "red": -100,
}

turtles = {}

# Create turtles
for color, y_pos in turtle_data.items():
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.setpos(-430, y_pos)
    t.speed(5)
    turtles[color] = t

# Ask user for their bet
bet = screen.textinput("Your Bet", "Choose the winning turtle color (purple, green, yellow, red):")

#Check if he inserted correct color
while bet not in turtle_data:
    bet = screen.textinput("Your Bet", "Choose the winning turtle color (purple, green, yellow, red):")
race_finished = False

while not race_finished:
    screen.delay(100)

    for color, t in turtles.items():
        t.forward(random.choice(range(10, 50, 10)))

        # Check if turtle reached finish line
        if t.xcor() >= 430:
            race_finished = True
            winner = color

            if bet == winner:
                print(f"You WIN! The {winner} turtle won!")
            else:
                print(f"You lost! The winner is the {winner} turtle.")
            break

screen.exitonclick()
