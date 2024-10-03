from turtle import Turtle, Screen
from pong import Ball, Paddle
import time

from scoreboard import ScoreBoard

WIDTH = 800
HEIGHT = 600
X = WIDTH //2
Y = HEIGHT // 2

screen = Screen()
screen.bgcolor("black")
screen.setup(width = WIDTH, height= HEIGHT)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

scoreboard = ScoreBoard()
scoreboard.draw_scoreboard()

screen.listen()

screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.hit_wall()
    if (ball.distance(left_paddle) < 50 and ball.xcor() < - 330 ) or (ball.distance(right_paddle) < 50 and ball.xcor() > 330):
        ball.hit_paddle()
        ball.move()
    if ball.xcor() > 380:
        scoreboard.inc_left()
        ball.refresh()
        time.sleep(0.5)
        scoreboard.draw_scoreboard()
    elif ball.xcor() < -380:
        scoreboard.inc_right()
        ball.refresh()
        time.sleep(0.5)
        scoreboard.draw_scoreboard()

screen.exitonclick()