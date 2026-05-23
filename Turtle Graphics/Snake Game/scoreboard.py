import turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}" , align = ALIGNMENT , font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()