from turtle import Turtle

class Kula(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(1, 1)
        self.shape("circle")
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):

        new_x = self.xcor()+self.move_x
        new_y = self.ycor()+self.move_y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.move_y *=-1
        self.move_speed *=0.95

    def bounce_x(self):
        self.move_x *=-1

    def reset_position(self):
        self.bounce_x()
        self.move_speed = 0.1
        self.goto(0,0)