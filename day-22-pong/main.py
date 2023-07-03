from turtle import Turtle, Screen
from paddle import Paddle, SEGMENT_SIZE
from ball import Ball, HSIZE, VSIZE
from scoreboard import Scoreboard
import time

XPOS = 0.9 * HSIZE / 2

screen = Screen()
screen.setup(width=HSIZE, height=VSIZE)
screen.bgcolor('black')
screen.title('THE PONG')
screen.tracer(0)

player1 = Paddle(-XPOS)
player2 = Paddle(XPOS)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

game_on = True
ball_counter = 0
while game_on:
    ball_counter += 1
    screen.update()
    time.sleep(.1)
    ball.animate()

    # detect hits with paddles
    if (ball.xcor() >= HSIZE/2 - (3 * SEGMENT_SIZE) and ball.distance(player2.position()) < 50) or \
       (ball.xcor() <= -HSIZE/2 + (3 * SEGMENT_SIZE) and ball.distance(player1.position()) < 50):
        print('test')
        ball.hit()
    #detect missing the ball with a paddle
    elif abs(ball.xcor()) >= HSIZE/2 - SEGMENT_SIZE/2:
        scoreboard.point(['p1', 'p2'][ball.xcor() < 0])
        time.sleep(1)
        ball.reset_position()
screen.exitonclick()
