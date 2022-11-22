from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.penup()
        self.goto(0,270)
        self.pendown()
        self.pencolor('white')
        self.score = 0
        self.hideturtle()
        self.showscore()

    def showscore(self):
        self.clear()
        self.write(f"Score = {self.score}   Highscore = {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.showscore()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.showscore()
