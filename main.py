from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def main():
    screen = Screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.listen()


    stop_game = False
    while stop_game == False:
        screen.update()
        sleep(0.1)
        snake.move_snake()
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        
        # Detect collision with wall.
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -291:
            stop_game = True

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                stop_game = True
    scoreboard.game_over()

    screen.exitonclick()


main()