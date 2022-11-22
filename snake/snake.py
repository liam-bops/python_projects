import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for pos in STARTING_POSITIONS:
            self.addsegment(pos)

    def addsegment(self,pos):
        new_segment = turtle.Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            current_segment = self.segments[i]
            next_segment = self.segments[i - 1]
            newx = next_segment.xcor()
            newy = next_segment.ycor()
            current_segment.goto(newx, newy)
        self.head.forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for i in self.segments:
            i.hideturtle()
        self.segments.clear()
        self.createsnake()
