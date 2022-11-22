from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.s1 = 0
        self.s2 = 0
        self.hideturtle()
        self.goto(0, 255)
        self.display()

    def display(self):
        self.write(f"Score\n{self.s1}   :   {self.s2}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.display()

    def gameover(self, s):
        self.goto(0, 0)
        self.write(f"GAME OVER {s} WINS!!!", False, align=ALIGNMENT, font=FONT)
