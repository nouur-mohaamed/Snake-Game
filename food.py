from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(name="circle")
        self.color("blue")
        self.resizemode("user")
        self.shapesize(0.5,0.5)
        self.penup()
        self.relocate_the_food()
    def relocate_the_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 270)
        self.goto(x=x, y=y)
