from turtle import *

pencolor('red')
pensize(1)
speed('fastest')

for i in range(6):
    fd(100) # forward distance
    lt(360/6)  # left turn
    for i in range(6):
        fd(150)
        lt(360/6)

hideturtle()
mainloop()