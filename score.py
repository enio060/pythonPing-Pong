from turtle import Turtle

class Score(Turtle):
    def __init__(self,pozycja):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(pozycja)
        self.points = 0
        self.write(self.points,align="center",font=("Courier",80,"normal"))

    def score(self):
        self.clear()
        self.points+=1
        self.write(self.points, align="center", font=("Courier", 80, "normal"))


def pasek():
    jd = Turtle()
    jd.penup()
    jd.color("white")
    jd.goto(0, 300)
    jd.setheading(270)
    jd.shapesize(2, 2)

    while jd.ycor() >= -300:
        jd.pendown()
        jd.forward(20)
        jd.penup()
        jd.forward(20)



