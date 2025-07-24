from turtle import *
import random as r

x_min = -5
x_max = 5
y_min = -5
y_max = 5
space = 0.1
func_list = ["x*x", "abs(x)", "0.5*x+1"]

setworldcoordinates(x_min, y_min, x_max, y_max)
speed(0)
pensize(3)


up()
goto(x_min, 0)
down()
goto(x_max, 0)

up()
goto(0, y_min)
down()
goto(0, y_max)


for func in func_list:
    color(r.choice(["green", "red", "blue","hot pink", "purple", "pink", "gray", "orange", "brown", "sky blue", "salmon"]))
    x = x_min
    y = eval(func)
    up()
    goto(x, y)
    down()

    while x <= x_max:
        x += space
        y = eval(func)
        goto(x, y) 

done()