import time
import turtle
from turtle import Turtle, Screen
from Snake import Snake
from food import Food


screen = Screen()
screen_width = 600
screen.screensize(screen_width, screen_width)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

border = Turtle()
border.penup()
border.goto(400,400)
border.shape("square")
border.color('white')
border.pensize(20)
border.pendown()
border.goto(400,-400)
border.goto(-400,-400)
border.goto(-400,400)
border.goto(400,400)
border.hideturtle()



def exit_game():
    turtle.exitonclick()


food = Food(screen, screen_width)
snake = Snake(screen_width)
screen.update()
loop = True

while loop:
    loop = snake.snake_loop(food)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()