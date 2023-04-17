from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.06)
    ball.move_ball()

    # Detect collision with top and bottom ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_ball_speed()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
