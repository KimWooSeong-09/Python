from turtle import *
import random as r

color_list = ['red', 'orange', 'yellow', 'lightgreen', 'green', 'blue', 'pink', 'hotpink', 'purple']

shape("turtle")
pensize(3)

for i in range(3):
    r_color = r.choice(color_list)
    color(r_color)
    fd(100)
    lt(120)

for i in range(4):
    r_color = r.choice(color_list)
    color(r_color)
    fd(100)
    lt(90)

for i in range(5):
    r_color = r.choice(color_list)
    color(r_color)
    fd(100)
    lt(72)

for i in range(6):
    r_color = r.choice(color_list)
    color(r_color)
    fd(100)
    lt(60)











