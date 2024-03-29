from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")

# create a snake body

# snake_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for snake_index in range(0, 3):
# for positions in snake_positions:
# snake = Turtle("square")
# snake.color("white")
# snake.penup()
# snake.goto(x=snake_x_positions[snake_index], y=0)
# snake.goto(positions)
# segments.append(snake)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail
        # trigger game_over


    # # for seg in segments:
    # # seg.forward(20)
# # for seg_num in range(start=2, stop=0, step=-1):
# for seg_num in range(len(segments) - 1, 0, -1):
# new_x = segments[seg_num - 1].xcor()
# new_y = segments[seg_num - 1].ycor()
# segments[seg_num].goto(new_x, new_y)
# segments[0].forward(20)


screen.exitonclick()
