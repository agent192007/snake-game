from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto((0, 320))
        self.write("Score : 0", align=ALIGNMENT, font=FONT)
        self.score = 0

    def update_score(self):
        self.score += 1
        self.clear()
        self.color('white')
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

