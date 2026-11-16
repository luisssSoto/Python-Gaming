import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from block import Block
from scoreboard import Scoreboard

wall = Wall()
for i in range(30):
    block = Block()
    wall.add_block(block)
wall.build_wall()

paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=1000, height=640)

screen.listen()

screen.onkey(paddle.move_forward, "Right")
screen.onkey(paddle.move_backward, "Left")

def hit_block(ball, idx, scoreboard):
        wall.break_block(idx)
        scoreboard.score_increased()
        ball.bounce_y()

screen.tracer(0)

is_it_over = False
while is_it_over is False:
    ball.move()

    for idx, block in enumerate(wall.container[:]):
        if block.isvisible() and ball.distance(block) < 30:
            hit_block(ball, idx, scoreboard)
            break

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() < -480 or ball.xcor() > 480:
        ball.bounce_x()

    if ball.distance(paddle) < 60 and ball.ycor() < -240:
        ball.bounce_y()

    if ball.ycor() < -280:
        scoreboard.end_game()
        is_it_over = True
        print("The Game is over")
    
    screen.update()
    time.sleep(0.03)


screen.exitonclick()