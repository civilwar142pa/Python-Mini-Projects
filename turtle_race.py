from turtle import Turtle as t, Screen
import random as r

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

colors = ["green", "blue", "red", "purple", "orange", "DeepPink"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

#umpire turtle
ump = t(shape="turtle")
ump.color("black")
ump.penup()
ump.right(90)
ump.goto(x=-50, y=180)

#racing turtles
for i in range(0,6):
    new_turtle = t(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                ump.write(f"        You won! The {winning_color} turtle is the winner!")
            else:
                ump.write(f"        You've lost! The {winning_color} turtle was the winner!")
            
        
        rand_distance = r.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()