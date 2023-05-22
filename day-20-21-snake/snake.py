from turtle import Turtle

SEGMENT_SIZE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self, color='white'):
        self.color = color
        self.body = [Turtle(), Turtle(), Turtle()]
        self.head = self.body[0]
        for i, segment in enumerate(self.body):
            segment.shape('square')
            segment.setx(i * -SEGMENT_SIZE)
            segment.color(color)
            segment.penup()

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].setx(self.body[i-1].xcor())
            self.body[i].sety(self.body[i-1].ycor())
        self.head.forward(SEGMENT_SIZE)

    def up(self):
        if not self.head.heading() % 180:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() % 180:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() % 180:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() % 180:
            self.head.setheading(LEFT)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(self.body[-1].position())
        self.body.append(new_segment)

