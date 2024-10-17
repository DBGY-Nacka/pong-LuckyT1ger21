from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 560)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
middle_line = Turtle()
middle_line.penup()
middle_line.goto(0, -560)
middle_line.pencolor("gray")
middle_line.pensize(7)
middle_line.pendown()
middle_line.goto(0, 560)
screen.update()
if __name__ == "__main__":

    game_is_on = True
    scoreboard = Scoreboard()
    ball = Ball()
    screen.listen()
    while game_is_on:
        for _ in range(500):
            screen.update()
            time.sleep(0.05)
            ball.move()
            print(ball.ycor())
            if ball.ycor() >= 280 or ball.ycor() <= -280:
                ball.bounce_angle()
            if ball.xcor() >= 400:
                ball.round_over(True)
            if ball.xcor() <= -400:
                ball.round_over(False)
        game_is_on = False
    screen.exitonclick()
