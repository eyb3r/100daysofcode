from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.level_display = Turtle()
        self.level_display.penup()
        self.level_display.goto(-250, 260)
        self.level_display.hideturtle()
        self.gover = Turtle()
        self.gover.hideturtle()
        self.gover.penup()

    def display_level(self):
        self.level_display.clear()
        self.level_display.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.gover.write("GAME OVER", font=FONT, align="center")

    def level_up(self):
        self.level += 1
