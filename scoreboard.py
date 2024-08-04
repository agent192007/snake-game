from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto((0, 280))
        self.current_text = "Score : 0"
        self.write(self.current_text, align='center')
        self.score = 0

    def update_score(self):
        self.score += 1
        self.color('black')
        self.write(self.current_text, align='center')
        self.color('white')
        self.current_text = f"Score : {self.score}"
        self.write(self.current_text, align='center')
