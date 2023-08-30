import time
from turtle import Screen
from snake import Snake, UP, RIGHT, LEFT, DOWN
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('snejk gejm')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard('data.txt')
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(.1)
    screen.update()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    #detect collision with wall
    if (snake.head.xcor() < -280 and snake.head.heading() == LEFT) \
        or (snake.head.xcor() > 280 and snake.head.heading() == RIGHT) \
        or (snake.head.ycor() > 280 and snake.head.heading() == UP) \
        or (snake.head.ycor() < -280 and snake.head.heading() == DOWN):
        scoreboard.restart()
        snake.restart()

    #detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.restart()
            snake.restart()
screen.exitonclick()
