from turtle import Turtle
from random import randint

WIDTH = 800
HEIGHT = 600
X = WIDTH //2
Y = HEIGHT // 2

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        self.penup()
        self.shape("circle")
        self.color("white")
        self.teleport(0, randint(-Y + 30, Y - 30))
        self.add_x = 10
        self.add_y = 10
        self.move_speed = 0.1

    def hit_wall(self):
        self.add_y = -self.add_y

    def hit_paddle(self):
        self.add_x = -self.add_x
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.add_x
        new_y = self.ycor() + self.add_y
        self.goto(new_x, new_y)




class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed('fast')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        y_cor = self.ycor()
        if y_cor + 80 <= Y:
            self.goto(self.xcor(), y_cor + 30)

    def move_down(self):
        y_cor = self.ycor()
        if y_cor - 80 >= -Y:
            self.goto(self.xcor(), y_cor - 30)



