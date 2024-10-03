from turtle import Turtle
WIDTH = 800
HEIGHT = 600
X = WIDTH //2
Y = HEIGHT // 2
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0

    def draw_line(self):
        self.penup()
        self.shapesize(stretch_wid=5)
        self.goto(0, -HEIGHT / 2 + 40)
        self.pendown()
        self.setheading(90)
        while self.ycor() <= (HEIGHT / 2 - 40):
            self.forward(20)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.hideturtle()

    def draw_scoreboard(self):
        self.clear()
        self.draw_line()
        self.goto(-100, Y - 100)
        self.write(f"{self.l_score}", align='center', font=('Courier', 80, 'bold'))
        self.goto(100, Y - 100)
        self.write(f"{self.r_score}", align='center', font=('Courier', 80, 'bold'))

    def inc_left(self):
        self.l_score += 1

    def inc_right(self):
        self.r_score += 1
