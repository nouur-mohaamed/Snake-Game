import turtle as t
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
#---------------------------------setting the screen up---------------------------------
screen=t.Screen()
screen.tracer(0) 
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("SNAKE GAME")
#---------------------------------creating the game objects---------------------------------
snake=Snake()
food=Food()
board=ScoreBoard()
#---------------------------------creating event listeners---------------------------------
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#---------------------------------the game loop---------------------------------
# create a flag controlling ending the game
game_on=True
# create a variable controlling the speed of the snake
sleep_time=0.1
while game_on:
    time.sleep(sleep_time)
    screen.update()
    snake.move()
    #detects collision with the food
    if snake.collided_with_food(food):
        food.relocate_the_food()
        board.increase_score()
        board.update_score()
        # increase the length of snake
        snake.extend_segments()
        # increase the speed of the snake
        sleep_time-=0.01
    # detects collision with the wall
    if snake.collided_with_wall():
        game_on=False
        board.game_over()
    #detect collision of head with snake segments
    if snake.collided_with_segments():
        print("collided")
        game_on = False
        board.game_over()






















screen.exitonclick()