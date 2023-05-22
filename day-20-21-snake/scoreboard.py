from turtle import Turtle
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", False, "center", FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
