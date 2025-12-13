from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import Score
import time


screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
print(score.h_score)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food collision
    if snake.head.distance(food) < 15:
        food.new_food()
        score.update_score()
        snake.increase_snake_body()

    # Wall collision
    if snake.hit():
        score.game_over()
        snake.reset()


    # Body collision
    if snake.body_collision():
        score.game_over()
        snake.reset()

screen.exitonclick()
