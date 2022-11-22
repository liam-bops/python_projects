import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
gameison = True
screen.listen()
screen.onkey(snake.right, 'd')
screen.onkey(snake.left, 'a')
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')

while gameison:
    screen.update()
    time.sleep(0.1)
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x < -280 or x > 280:
        scoreboard.gameover()
        gameison = False
    if y < -280 or y > 280:
        scoreboard.gameover()
        gameison = False
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment)<10:
                scoreboard.gameover()
                gameison = False



screen.exitonclick()
