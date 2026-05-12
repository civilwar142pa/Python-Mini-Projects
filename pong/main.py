#imports
from turtle import Screen as s
from paddle import Paddle as p
from ball import Ball as b
from scoreboard import Scoreboard as sb
from level import Level as l
import time as t
  
#screen
screen = s()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong") 
screen.tracer(0)  
screen.colormode(255) 

#scoreboard
scoreboard = sb()

#user paddle
r_paddle = p((350,0))

#computer paddle
l_paddle = p((-350,0))

#ball
ball = b()

#level counter
level = l()


#controls
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

level.next_level()

#game loop
game_on = True
while game_on:
    t.sleep(0.1)
    screen.update()
    ball.move()

    #bouncy ball
    if ball.ycor() > 270 or ball.ycor() < -270:
       ball.bounce_y()
    elif ball.distance(r_paddle) < 40 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        ball.bounce_x()
        
    #score detection
    if ball.xcor() < -390:
        scoreboard.update_score("r")
        ball.goto(0,0)
        if scoreboard.right_score < 10:
            level.level_counter()
    elif ball.xcor() > 390:
        scoreboard.update_score("l")
        ball.goto(0,0)
        if scoreboard.left_score < 10:
            level.level_counter()
        
        
    #loss detection
    if scoreboard.left_score == 10:
        scoreboard.game_over("left")
        game_on = False
    elif scoreboard.right_score == 10:
        scoreboard.game_over("right")
        game_on = False
        

screen.exitonclick()