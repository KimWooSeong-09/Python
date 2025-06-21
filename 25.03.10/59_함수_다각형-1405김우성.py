from turtle import *

def input_data():
    x, y = map(int, input("이동할 좌표(a, b) : ").split())
    return x, y


def moving():
    a, b = input_data()
    up()
    goto(a, b)
    down()


def polygon():
    n, a = map(int, input("종류(3이상) 한변(5이상) : ").split())
    for i in range(1, n + 1):
        fd(a)
        lt(360 // n)
        color("black")
    return n, a

# Main

while True:
    print("=== 도형 그리기 ===")
    moving()
    polygon()
    
    
    con = int(input("계속(y(1)) n(그 외): "))
    if con != 1:
        break

exitonclick()
