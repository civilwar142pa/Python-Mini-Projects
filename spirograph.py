#get the turle to draw a spirograph
#circles 100 units in diameter

import turtle as t
import random 

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    return (r,g,b)

def draw_circle(turtle):
    color = random_color()
    turtle.pencolor(color)
    turtle.circle(100, None, None)
    
def draw_spirograph(turtle):
    turtle.speed("fastest")
    for i in range(75):
        draw_circle(turtle)
        turtle.right(5)



timmy = t.Turtle()
t.colormode(255)
timmy.shape("circle")
timmy.color("blue")
timmy.width(1)
timmy.hideturtle()
draw_spirograph(timmy)


screen = t.Screen()
screen.exitonclick()