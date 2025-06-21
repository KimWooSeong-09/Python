from turtle import *
import random as r

#x 좌표 범위
x_min = -5; x_max = 5

#y 좌표 범위
y_min = -5; y_max = 5

# 그래프 간격
space = 0.1

# 함수 리스트
func_list = ["x+x", "abs(x)", "0.5*x + 1"]

# 사용자 정의 좌표 설정, 거북 속도, 선 굵기
setworldcoordinates(x_min, y_min, x_max, y_max)
speed(0)
pensize(3)

# x축 그리기
up(); goto(x_min, 0)
down(); goto(x_max, 0)

# y축 그리기
up(); goto(y_min, 0)
down(); goto(y_max, 0)

# 그래프 그리기
for func in func_list:
    color(r.choice["green", "red", "blue", "purple"])
    x = x_min
    y = eval(func)
    up()
    goto