from turtle import *

user_input = int(input("몇각형을 그리고 싶은지 숫자로 입력해주세요 : "))
user_cinput = input("설정 하고싶은 컬러를 영어로 입력해주세요 : ")

angle = 360 // user_input

pensize(3)
for i in range(user_input):
    color(user_cinput)
    fd(50)
    lt(angle)

exitonclick()
    
    
