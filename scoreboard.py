from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans", 35, "normal")
POSITION_L = (200, 160)
POSITION_R = (-200, 160)


class Scoreboard(Turtle):

    def __init__(self, name1="Player1", name2="Player2"):
        super().__init__()
        self.name1 = name1
        self.name2 = name2
        self.score_l = 0
        self.score_r = 0
        self.color("Gray")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(POSITION_L)
        self.write(f"{self.name2}: {self.score_l}",
                   align=ALIGNMENT, font=FONT)
        self.goto(POSITION_R)
        self.write(f"{self.name1}: {self.score_r}",
                   align=ALIGNMENT, font=FONT)

    def game_over(self, Player2Won):
        self.clear()
        self.goto(0, 0)
        self.color("Blue")
        if Player2Won:
            self.write(f"GAME OVER \n Player: {self.name1} Won! \n With {self.score_r} Score!",
                       align=ALIGNMENT, font=FONT)
        else:
            self.write(f"GAME OVER \n Player: {self.name2} Won! \n With {self.score_l} Score!",
                       align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()
