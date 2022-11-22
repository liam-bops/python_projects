from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()
screen = Screen()
screen.tracer(0)
ball = Ball()
p1 = Paddle()
p2 = Paddle()
screen.setup(width=820, height=620)
p1.move(380, 0)
p2.move(-380, 0)
gameison = True
screen.listen()
screen.onkeypress(p2.up, 'w')
screen.onkeypress(p2.down, 's')
screen.onkeypress(p1.up, 'Up')
screen.onkeypress(p1.down, 'Down')
while gameison:
    screen.update()
    time.sleep(0.0125)
    ball.forward(10)
    # print('(p1.parts[1].distance(ball)',p1.parts[1].distance(ball))
    # print('(p1.parts[2].distance(ball)', p1.parts[2].distance(ball))
    if p2.parts[1].distance(ball) <= 20:
        ball.setheading(0)
    elif p2.parts[2].distance(ball) <= 20:
        ball.setheading(45)
    elif p2.parts[0].distance(ball) <= 20:
        ball.setheading(315)
    if p1.parts[1].distance(ball) <= 20:
        ball.setheading(180)
    elif p1.parts[2].distance(ball) <= 20:
        ball.setheading(135)
    elif p1.parts[0].distance(ball) <= 20:
        ball.setheading(225)
    if ball.ycor() < -300:
        cur = ball.heading()
        if cur == 315:
            new = 45
        elif cur == 225:
            new = 135
        ball.setheading(new)
    if ball.ycor() > 300:
        cur = ball.heading()
        if cur == 135:
            new = 225
        elif cur == 45:
            new = 315
        ball.setheading(new)
    if ball.xcor() > 400:
        scoreboard.s1 += 1
        ball.home()
        scoreboard.update()
        p1.move(380, 0)
        p2.move(-380, 0)
        time.sleep(1)
    if ball.xcor() < -400:
        scoreboard.s2 += 1
        ball.home()
        p1.move(380, 0)
        p2.move(-380, 0)
        scoreboard.update()
        time.sleep(1)
    if scoreboard.s1 >= 5:
        gameison = False
        scoreboard.gameover('PLAYER 1')
    if scoreboard.s2 >= 5:
        gameison = False
        scoreboard.gameover('PLAYER 2')

screen.exitonclick()
