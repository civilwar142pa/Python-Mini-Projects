from turtle import Turtle as t
import random as r

SPEED="fastest"
MOVE_DISTANCE=20

class Ball(t):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.up()
        self.speed(SPEED)
        self.x_move = r.choice([-10, 10])
        self.y_move = r.choice([-10, 10])
        self.degrees(360)
    
    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
    
