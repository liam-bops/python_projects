from turtle import Turtle


class Paddle():

    def __init__(self):
        self.parts = [0, 0, 0]
        self.parts[0] = Turtle()
        self.parts[1] = Turtle()
        self.parts[2] = Turtle()
        self.createpaddle()
        # self.parts[0].color('green')
        # self.parts[1].color('blue')
        # self.parts[2].color('red')

    def createpaddle(self):
        for part in self.parts:
            part.penup()
            part.shape('square')
            part.setheading(90)
            part.shapesize(stretch_len=2, stretch_wid=0.5)

    def up(self):
        self.parts[1].forward(20)
        self.parts[2].forward(20)
        self.parts[0].forward(20)

    def down(self):
        self.parts[1].back(20)
        self.parts[2].back(20)
        self.parts[0].back(20)

    def move(self, x, y):
        self.parts[1].goto(x, y)
        self.parts[2].goto(x, y + 40)
        self.parts[0].goto(x, y - 40)
