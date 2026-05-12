from turtle import Turtle as t
import random 

ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')

class Scoreboard(t):
    
    def __init__(self):
        super().__init__()
        self.up()
        self.color("yellow")
        self.goto(0, 260)
        self.speed("fastest")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    def update_score(self, scorer):
        if scorer == "l":
            self.left_score += 1
        elif scorer == "r":
            self.right_score += 1
        
        self.update_scoreboard()  
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score}     |     {self.right_score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self, winner):
        self.goto(0, 230)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color(r, g, b)
        
        if winner == "left":
            self.write("LEFT WINS!", align=ALIGNMENT, font=FONT)
            self.goto(0, self.ycor()-30)
        elif winner == "right":
            self.write("RIGHT WINS!", align=ALIGNMENT, font=FONT)
            self.goto(0, self.ycor()-30)
        
        for i in range(0,16):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            self.color(r, g, b)
            self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
            self.goto(0, self.ycor()-30)
            