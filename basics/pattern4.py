from turtle import *
from random import randint, choice
squares = 0
speed('fastest')
while squares < 100:
    x = randint(-300, 300)
    y = randint(-300, 300)
    size = randint(50, 100)
    penup()
    goto(x, y)
    pendown()
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    fillcolor(choice(colors))
    begin_fill()
    for i in range(6):
        fd(size)
        circle(size/4)
        rt(360/6)
    end_fill()
    squares += 1
hideturtle()
mainloop()