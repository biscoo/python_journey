from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x_pos, 0)
            self.snake_body.append(segment)
            x_pos -= 20

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movement controls
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # Wall collision
    def hit(self):
        if abs(self.head.xcor()) > 470 or abs(self.head.ycor()) > 370:
            return True
        return False

    # Add body segment
    def increase_snake_body(self):
        last = self.snake_body[-1]
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(last.xcor(), last.ycor())
        self.snake_body.append(segment)

    # Body collision
    def body_collision(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
