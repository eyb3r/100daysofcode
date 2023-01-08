from random import random


def pick_color():
    return tuple([int(255*x) for x in [random(), random(), random()]])


def draw_shapes(ttt):
    for i in range(4, 11):
        ttt.pencolor(pick_color())
        for _ in range(i):
            ttt.forward(100)
            ttt.right(360/i)


def random_walk(ttt):
    ttt.pensize(5)
    ttt.speed(10)
    for _ in range(500):
        ttt.pencolor(pick_color())
        ttt.forward(25)
        ttt.right(int(4*random())*90)


def spirograph(number):
    if number == 0:
        return "be serious"
    ttt.speed(20)

    for _ in range(number):
        ttt.pencolor(pick_color())
        ttt.circle(100, steps=1000)
        ttt.right(360/number)
