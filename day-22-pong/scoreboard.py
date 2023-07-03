from turtle import Turtle
FONT = ("Courier", 60, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.p1score = 0
        self.p2score = 0
        self.color("white")
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"{self.p1score} : {self.p2score}", False, "center", FONT)

    def point(self, player):
        if player == 'p1':
            self.p1score += 1
        elif player == 'p2':
            self.p2score += 1
        else:
            pass
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
