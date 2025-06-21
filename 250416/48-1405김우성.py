#사각형

from turtle import *

shape("turtle")
color("hotpink")
pensize(3)

for i in range(4):
    fd(100)
    lt(90)

#삼각형
color("skyblue")
for i in range(3):
    fd(100)
    lt(120)

color("yellow")
circle(50)