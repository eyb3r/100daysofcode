import random
from turtle import Turtle, Screen
# import colorgram
#
# palette = [tuple(c.rgb) for c in colorgram.extract('hirst.jpg', 50)]
ttt = Turtle()
ttt.speed(20)
ttt.penup()
ttt.hideturtle()

screen = Screen()
screen.colormode(255)

palette = [(210, 153, 64), (240, 232, 237), (39, 86, 172), (103, 160, 209), (229, 199, 57), (180, 61, 100), (148, 19, 59), (199, 115, 157), (143, 181, 10), (189, 72, 39), (51, 110, 95), (12, 66, 135), (187, 78, 103), (96, 107, 170), (221, 172, 191), (140, 167, 162), (171, 187, 220), (183, 101, 85), (228, 174, 167), (184, 194, 198), (104, 140, 131), (173, 205, 199)]

ttt.goto(-300,-300)
print(ttt.pos())

for _ in range(100):
    ttt.dot(20, random.choice(palette))
    x = (ttt.xcor() + 60)
    y = ttt.ycor()
    if x >= 300:
        x -= 600
        y += 60
    ttt.goto(x, y)


screen.exitonclick()
