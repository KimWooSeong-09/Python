from turtle import *

pensize(3)
speed(0)
bgcolor("black")
x = 1

for i in range(200):
    if i % 3 == 0:
        color("red")
    elif i % 3 == 1:
        color("yellow")
    else:
        color("blue")
    x += 1
    fd(x)
    lt(119)
