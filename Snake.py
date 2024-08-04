from turtle import Turtle
import turtle


class Snake:
    def __init__(self, width):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.direction = 'left'
        self.screen_width = width
        self.edge = self.screen_width // 2
        self.clicked = False
        self.last_pop = ()

        for position in self.positions:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def cords(self):
        return self.positions

    def snake_loop(self,food):
        def move(key):
            if key == 'w':
                if self.direction in ['left', 'right'] and self.clicked is False:
                    self.direction = 'up'
                    self.clicked = True

            elif key == "s":
                if self.direction in ['left', 'right'] and self.clicked is False:
                    self.direction = 'down'
                    self.clicked = True

            elif key == 'a':
                if self.direction in ['up', 'down'] and self.clicked is False:
                    self.direction = 'left'
                    self.clicked = True

            elif key == 'd':
                if self.direction in ['up', 'down'] and self.clicked is False:
                    self.direction = 'right'
                    self.clicked = True




        self.clicked = False
        turtle.onkey(lambda: move('w'), 'w')
        turtle.onkey(lambda: move('s'), 's')
        turtle.onkey(lambda: move('a'), 'a')
        turtle.onkey(lambda: move('d'), 'd')
        turtle.listen()

        temp = list(self.positions[-1])
        if self.direction == "left":
            temp[0] -= 20
        elif self.direction == "down":
            temp[1] -= 20
        elif self.direction == "up":
            temp[1] += 20
        elif self.direction == "right":
            temp[0] += 20
        self.positions.append(tuple(temp))

        if food.cord != self.positions[-1]:
            self.positions.pop(0)
        else:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            self.segments.append(new_segment)
            food.food_eaten()

        for position, segment in zip(self.positions, self.segments):
            segment.goto(position)
