from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
POSITION_L = ()
POSITION_R = ()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.goto(POSITION_L)
        self.update_scoreboard_l()
        self.hideturtle()

    def update_scoreboard_l(self):
        self.write(f"Score: {self.score_l}", align=ALIGNMENT, font=FONT)

    def update_scoreboard_r(self):
        self.write(f"Score: {self.score_r}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard_l()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard_r()
