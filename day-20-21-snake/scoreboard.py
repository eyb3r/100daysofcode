from turtle import Turtle
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self, file_handle):
        super().__init__()
        self.goto(0, 280)
        self.score = 0
        self.file_handle = file_handle
        with open(file_handle, 'r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}, High score: {self.high_score}", False, "center", FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.show_score()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.file_handle, 'w') as file:
                file.write(str(self.high_score))

        self.score = -1
        self.refresh()
        #self.goto(0, 0)
        #self.write(f"Game Over", False, "center", FONT)

