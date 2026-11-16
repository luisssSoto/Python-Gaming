from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        # super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x = 10
        self.y = 10
        self.increase_speed = 0.1

    def move(self):
        '''How the ball moves'''
        new_x = self.xcor() - self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        '''How the ball bounces against the paddle and the wall'''
        self.y *= -1
        self.increase_speed *= 0.9
        
    def bounce_x(self):
        '''How the ball bounces against the left and right walls'''
        self.x *= -1

    def restart(self):
        '''Restart the match once the ball goes beyond the limits'''
        self.goto(0, 0)
        self.increase_speed = 0.1
        self.bounce_y
        

    
    