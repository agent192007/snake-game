from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen, screen_width):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("blue")
        self.window = screen
        self.max_cord = (screen_width / 4) - 20
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        while True:
            x = random.randint((-self.max_cord) // 10, self.max_cord // 10)
            y = random.randint((-self.max_cord) // 10, self.max_cord // 10)
            self.cord = (x * 20, y * 20)
            if self.cord not in self.positions:
                break
        self.goto(self.cord)

    def food_eaten(self):
        while True:
            x = random.randint((-self.max_cord) // 10, self.max_cord // 10)
            y = random.randint((-self.max_cord) // 10, self.max_cord // 10)
            self.cord = (x * 20, y * 20)
            if self.cord not in self.positions:
                break
        self.goto(self.cord)

