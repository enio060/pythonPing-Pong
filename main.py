from turtle import Screen
from Paddle import Paddle
from kula import Kula
import time
from score import Score,pasek


scr = Screen()
scr.tracer(0)
scr.setup(800,600)
scr.bgcolor("black")
scr.title("Pong")


paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
kulka = Kula()
score1 = Score((80,200))
score2 = Score((-80,200))
pasek()
scr.listen()
scr.onkey(paddle1.go_up,"Up")
scr.onkey(paddle1.go_down,"Down")
scr.onkey(paddle2.go_up,"w")
scr.onkey(paddle2.go_down,"s")


is_on = True
while is_on:
    time.sleep(kulka.move_speed)
    scr.update()
    kulka.move()
    if kulka.ycor() > 280 or kulka.ycor() < -280 :
        kulka.bounce_y()

    if kulka.xcor() > 380:
        kulka.reset_position()
        score1.score()
    elif kulka.xcor() < -380 :
        kulka.reset_position()
        score2.score()

    if kulka.distance(paddle1) < 50 and kulka.xcor() > 320 or kulka.distance(paddle2) < 50 and kulka.xcor() < -320:
        kulka.bounce_x()





scr.exitonclick()
