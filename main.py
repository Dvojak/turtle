from turtle import *
from random import *
shape("turtle")




def spirala():
    home()
    clear()
    bgcolor('black')
    color = ['red','dark red']
    speed(900)
    for numbers in range(400):
     forward(numbers + 1 )
     right(89)
     pencolor(color[numbers % 2])

def hvezdicnik():
    home()
    clear()
    speed(400)
    bgcolor("black")
    color("yellow")
    penup()
    right(45)
    forward(100)
    pendown()
    for i in range (30):
        forward(150)
        left(120)
        forward(150)
        right(45)


def domek():
    home()
    clear()
    forward(200)
    left(90)
    forward(150)
    left(45)
    forward(100)
    left(45)
    forward(100)
    left(45)
    forward(100)
    left(45)
    forward(150)
    left(90)
    forward(50)


def jmeno():
    home()
    clear()


vyber = 1

while vyber != 0:
    vyber = numinput("Výběr", "1 - spirála\n 2 - hvezdicka\n 3 - domek\n 4 - jmeno\n 0 - Konec")
    if vyber == 1:
        spirala()
    if vyber == 2:
        hvezdicnik()
    if vyber == 3:
        domek()
    if vyber == 4:
        jmeno()
