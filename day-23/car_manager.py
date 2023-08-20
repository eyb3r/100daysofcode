from turtle import Turtle
from random import choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
LANES = [-240, -210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240]


class Car(Turtle):
    def __init__(self, color, ypos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(1.0, 2.0, 0)
        self.color(color)
        self.goto(300, ypos)
        self.setheading(180)

    def ride(self, stepsize):
        self.forward(stepsize)


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_car()
        self.tempo_control = 0
        self.stepsize = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if len(self.cars) < 20:
            self.cars.append(Car(choice(COLORS), choice(LANES)))

    def traffic(self):
        self.tempo_control += 1
        if self.tempo_control == 5:
            self.tempo_control = 0
            self.generate_car()

        for car in self.cars:
            car.ride(self.stepsize)
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
                self.generate_car()

    def increase_difficulty(self):
        self.stepsize += MOVE_INCREMENT
