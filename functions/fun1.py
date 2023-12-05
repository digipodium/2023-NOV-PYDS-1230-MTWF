from turtle import *
# square function - define
def square():
    pensize(5)
    fillcolor('yellow')
    begin_fill()
    for i in range(4):
        fd(120)
        lt(90)
    end_fill()

speed('fastest')
pencolor('red')
square() # square function - call/use
goto(-100, 100)
pencolor('blue')
square() 
goto(100, -100)
pencolor('green')
square()

hideturtle()
mainloop()