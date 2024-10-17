from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color("white")
        self.speed(1)
        self.penup()
        self.goto(0, 0)
        self.right_initial_angle()

    def right_initial_angle(self):
        self.setheading(randint(-60, 60))

    def left_initial_angle(self):
        self.setheading(randint(120, 240))

    def bounce_angle(self):
        self.setheading(360-self.heading()+randint(-10, 10))

    def move(self):
        self.forward(10)

    def round_over(self, right_won):
        self.goto(0, 0)
        if right_won:
            self.left_initial_angle()
        else:
            self.right_initial_angle()
