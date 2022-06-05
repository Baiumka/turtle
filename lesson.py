from turtle import *

class Figure(Turtle):
    def __init__(self, my_color, my_shape, my_speed, x, y):
        super().__init__()
        self.color(my_color)
        self.shape(my_shape)
        self.speed = my_speed
        self.penup()
        self.goto(x,y)
    def move_up(self):
       self.goto(self.xcor(), self.ycor() + self.speed)
    def move_down(self):
       self.goto(self.xcor(), self.ycor() - self.speed)
    def move_left(self):
       self.goto(self.xcor() - self.speed, self.ycor())
    def move_right(self):
       self.goto(self.xcor() + self.speed, self.ycor())

        
class Finish(Figure):
    def __init__(self, my_speed, x, y):
        super().__init__("green", "circle", my_speed, x, y)


class Enemy(Figure):
    def __init__(self, my_speed, x, y):
        super().__init__("red", "square", my_speed, x, y)


class Player(Figure):
    def __init__(self, my_color, my_speed, x, y):
        super().__init__(my_color, "turtle", my_speed, x, y)
        self.left(90)
    def is_collide(self, figure):
        dist = self.distance(figure.xcor(), figure.ycor())
        if dist < 15:
            return True
        else:
            return False





f1= Finish(0, 0, 200)
e1 = Enemy(5, 200, 100)
e2 = Enemy(5, -200, 110)
p1 = Player("orange", 10, 0, -200)


scr = p1.getscreen()
scr.listen()

scr.onkey(p1.move_up,"W")
scr.onkey(p1.move_left,"A") 
scr.onkey(p1.move_down,"S")
scr.onkey(p1.move_right,"D")

while True:
    if e1.xcor() > 200 or e1.xcor() < -200:
        e1.speed = -e1.speed
    if e2.xcor() > 200 or e2.xcor() < -200:
        e2.speed = -e2.speed

    e2.move_right()
    e1.move_left()

    if p1.is_collide(f1):
        print("Победа")

    if p1.is_collide(e1):
        print("Первый противник вас поймал")

    if p2.is_collide(e2):
        print("Первый противник вас поймал")

