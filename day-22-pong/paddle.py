from turtle import Turtle

SEGMENT_SIZE = 20
PADDLE_SIZE = 5


class Paddle(Turtle):
    def __init__(self, xpos, color='white'):
        super().__init__()
        super().shape('square')
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, 0)

    def up(self):
        if self.ycor() <= 350:
            self.goto(self.xcor(), self.ycor() + SEGMENT_SIZE)

    def down(self):
        if self.ycor() >= -350:
            self.sety(self.ycor() - SEGMENT_SIZE)
