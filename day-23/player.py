from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.move_to_start()

    def step(self):
        self.forward(MOVE_DISTANCE)

    def crossed_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def move_to_start(self):
        self.goto(STARTING_POSITION)
