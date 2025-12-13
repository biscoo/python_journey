
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score_val = 0
        with open("high_score.txt") as file:
            self.h_score = int(file.read())
        self.goto(0, 360)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score_val} High score: {self.h_score}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score_val += 1
        self.clear()
        self.write_score()

    def game_over(self):
        if self.score_val > self.h_score:
            self.h_score = self.score_val
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.h_score))
        self.score_val = 0
        self.write_score()
        return True
