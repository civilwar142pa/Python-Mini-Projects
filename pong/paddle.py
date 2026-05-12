from turtle import Turtle as t

SPEED = "fastest"
MOVE_DISTANCE = 20

class Paddle(t):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.up()
        self.speed(SPEED)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        
    def go_up(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)
        
    def go_down(self):
        self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)
        
    
        
        
        