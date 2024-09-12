from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed(1)
        self.penup()

    def move(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)
