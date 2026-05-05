import turtle as t
import random as r

color_list = [(250, 138, 53), (46, 172, 91), (119, 185, 139), (248, 74, 109),
              (246, 222, 62), (248, 77, 48), (119, 119, 66), (11, 42, 108), 
              (51, 147, 26), (7, 108, 163), (153, 76, 127), (252, 168, 158), 
              (238, 215, 9), (197, 201, 31), (6, 57, 124), (222, 124, 150), 
              (135, 164, 192), (160, 212, 176), (243, 160, 178), (106, 122, 160),
              (179, 187, 210), (52, 173, 180), (153, 208, 218), (74, 112, 11),
              (24, 117, 5)]

def line_of_circles(turtle,color_list):
    #draws a line of filled circles
    for i in range (5):
        turtle.down()
        color = random_color(color_list)
        print(color)
        turtle.pencolor(color)
        turtle.circle(10, None, None)
        turtle.up()
        turtle.forward(75)
        

def random_color(color_list):
    #gets a random color from list
    index = r.randint(0, len(color_list)-1)
    color = color_list[index]
    return color

def reset_line(turtle):
    #moves turtle to beginning of next line
    turtle.up()
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward((75*5)+20)
    turtle.right(180)
    turtle.forward(20)
    turtle.down()


dot = t.Turtle()
dot.speed("fastest")
t.colormode(255)
dot.width(20)
dot.hideturtle()

#starting position
dot.up()
dot.left(180)
dot.forward(200)
dot.right(90)
dot.forward(200)
dot.right(90)


for i in range(6):
    line_of_circles(dot, color_list)
    reset_line(dot)


screen = t.Screen()
screen.exitonclick()