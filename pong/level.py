from turtle import Turtle as t
import time

ALIGNMENT = "center"
FONT = ('Courier', 30, 'bold')

class Level(t):
    
    def __init__(self):
        super().__init__()
        self.up()
        self.color("yellow")
        self.goto(0, 100)
        self.speed("fastest")
        self.hideturtle()
        self.level = 1
        
    def level_counter(self):
        self.clear()
        self.level += 1
        self.next_level()
        
    def next_level(self):
        self.write(f"GET READY FOR LEVEL {self.level} IN...", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("---- 3 ----", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("---- 2 ----", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("---- 1 ----", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("---- GO! ----", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(0.5)
        self.clear()
        
        
        
        