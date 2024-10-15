from turtle import *
from random import *

shape("turtle")

def spirala():
    """Kreslí spirálu, která se postupně zvětšuje."""
    home()
    clear()
    bgcolor('black')
    color = ['red', 'dark red']
    speed(900)
    for numbers in range(400):
        forward(numbers + 1)
        right(89)
        pencolor(color[numbers % 2])

def hvezdicnik():
    """Kreslí sérii hvězd, které vytvoří unikátní tvar."""
    home()
    clear()
    speed(400)
    bgcolor("black")
    color("yellow")
    penup()
    right(45)
    forward(100)
    pendown()
    for i in range(30):
        forward(150)
        left(120)
        forward(150)
        right(45)

def domek():
    """Kreslí jednoduchý domek."""
    home()
    clear()
    speed(10)
    forward(200)
    left(90)
    for i in range(4):
        forward(150)
        left(45)
    forward(150)
    left(90)
    forward(200)

def chaos():
    """Kreslí chaotické čáry s náhodnou rychlostí, šířkou a směrem."""
    home()
    clear()
    x = randint(5, 20)
    i = 0
    while i != x:
        i += 1
        speed(randint(1, 10))
        width(randint(1, 10))
        forward(randint(1, 400))
        left(randint(1, 400))
        forward(randint(1, 400))
        right(randint(1, 400))

vyber = 1

while vyber != 0:
    vyber = numinput("Výběr", "1 - spirála\n 2 - hvezdicka\n 3 - domek\n 4 - chaos\n 0 - Konec")
    if vyber == 1:
        spirala()
    if vyber == 2:
        hvezdicnik()
    if vyber == 3:
        domek()
    if vyber == 4:
        chaos()
