import turtle as t
from food import Food
#set our constants
STARTING_X_POSITIONS=[0, -10, -20]
MOVEMENT_STEP=10
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        #initialize our fields
        self.snake_body_segments = []
        self.head_of_the_snake=None
        # creating the snake
        self.create_snake()

    def create_segment(self,position):
        new_segment = t.Turtle(shape="square")
        new_segment.color("white")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        return new_segment
    def create_snake(self):
        for x in STARTING_X_POSITIONS:
            self.snake_body_segments.append(self.create_segment(position=(x,0)))
        self.head_of_the_snake = self.snake_body_segments[0]

    def extend_segments(self):
        last_segment_x_position=self.snake_body_segments[-1].xcor()
        last_segment_y_position=self.snake_body_segments[-1].ycor()
        self.snake_body_segments.append(self.create_segment(position=(last_segment_x_position,last_segment_y_position)))


    def move(self):
        for idx in range(len(self.snake_body_segments)-1,0,-1):
            new_position=self.snake_body_segments[idx-1].position()
            self.snake_body_segments[idx].goto(new_position)
        self.head_of_the_snake.forward(MOVEMENT_STEP)

    def up(self):
        if self.head_of_the_snake.heading()!=DOWN:
            self.head_of_the_snake.setheading(UP)
    def down(self):
        if self.head_of_the_snake.heading()!=UP:
            self.head_of_the_snake.setheading(DOWN)
    def left(self):
        if self.head_of_the_snake.heading()!=RIGHT:
            self.head_of_the_snake.setheading(LEFT)
    def right(self):
        if self.head_of_the_snake.heading() != LEFT:
            self.head_of_the_snake.setheading(RIGHT)

    def collided_with_food(self,food:Food):
        if self.head_of_the_snake.distance(food)<10:
            return True
        return False
    def collided_with_wall(self):
        if self.head_of_the_snake.xcor()>290 or self.head_of_the_snake.xcor()<-290 or self.head_of_the_snake.ycor()>290 or self.head_of_the_snake.ycor()<-290:
            return True
        return False
    def collided_with_segments(self):
        for segment in self.snake_body_segments[1:]:
            if self.head_of_the_snake.distance(segment)<8:
                return True
        return False



