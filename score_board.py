from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=275)
        self.update_score()
    def increase_score(self):
        self.score+=1
    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}", align="center", font=('arial', 15, 'normal'))
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align="center", font=('arial', 15, 'normal'))

