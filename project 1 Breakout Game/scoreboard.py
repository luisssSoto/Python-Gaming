"""Scoreboard class"""

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.goto(0, 280)
        self.write(arg=self.score, align="center", font=('Courier', 20, "bold"))
    
    def score_increased(self):
        self.score += 10
        self.update_score()

    def end_game(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"You Lost Score: {self.score}", align="center", font=("Courier", 20, "bold"))

