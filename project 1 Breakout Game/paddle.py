"""Paddle Class"""

from turtle import Turtle

STEPS = 20

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        # super().__init__(coordinates)
        # Turtle.__init__(self, coordinates)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.setheading(0)
        self.speed("fastest")
        self.penup()
        self.goto(coordinates)

    def move_forward(self):
        self.forward(50)
    
    def move_backward(self):
        self.backward(50)

