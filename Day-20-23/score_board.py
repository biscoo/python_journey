from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score_val = 0
        self.goto(0, 360)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score_val}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score_val += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))
        return True
