from turtle import Turtle

from paddle import SEGMENT_SIZE


HSIZE = 1000
VSIZE = 800


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.setheading(45)
        self.bouncing = False
        self.x_diff = SEGMENT_SIZE/2
        self.y_diff = SEGMENT_SIZE/2

    def animate(self):
        self.goto(self.xcor()+self.x_diff, self.ycor()+self.y_diff)
        if abs(self.ycor()) >= VSIZE/2-SEGMENT_SIZE/2:
            self.y_diff *= -1 #bounce from top/bottom

    def hit(self):
        self.x_diff *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.hit()

