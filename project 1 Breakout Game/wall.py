from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.container = []
        self.x = -460
        self.y = 240

    def add_block(self, block):
        '''Adding a block to the container'''
        self.container.append(block)

    def build_wall(self):
        '''Building a row of blocks'''
        for i, block in enumerate(self.container):
            if i == 15:
                self.y -= 40
                self.x = -460
            block.goto(self.x,  self.y)
            self.x += 65

    def break_block(self, idx):
        self.container[idx].hideturtle()
        #self.container[idx].teleport(self.container[idx].xcor(), self.container[idx].ycor() + 100)
        