from turtle import *
import random

# 플레이어 거북이
tc = Turtle()
tc.shape("turtle")
tc.color("white")
tc.up()
tc.speed(0)

# 먹이
tf = Turtle()
tf.shape("circle")
tf.color("green")
tf.up()
tf.speed(0)

# 추격자
tv = Turtle()
tv.shape("turtle")
tv.color("red")
tv.up()
tv.speed(0)

# 게임 상태 변수
game_running = True

# 화면 설정
def ready():
    setup(500, 500)
    title("Turtle Eat Game")
    bgcolor("orange")

# 방향 조작
def turn_right():
    tc.setheading(0)
def turn_left():
    tc.setheading(180)
def turn_up():
    tc.setheading(90)
def turn_down():
    tc.setheading(270)

# 먹이 랜덤 위치 이동
def move_food():
    x = random.randint(-230, 230)
    y = random.randint(-230, 230)
    tf.goto(x, y)

# 게임 종료 처리
def game_over():
    global game_running
    game_running = False
    tf.hideturtle()
    tc.hideturtle()
    tv.hideturtle()

    # 메시지 출력
    msg = Turtle()
    msg.hideturtle()
    msg.color("black")
    msg.write("Game Over!", align="center", font=("Arial", 24, "bold"))

# 게임 루프
def play():
    if not game_running:
        return

    # 플레이어 이동
    tc.forward(10)

    # 먹이에 닿았는지 체크
    if tc.distance(tf) < 20:
        move_food()

    # 추격자(tv)가 먹이(tf)를 향해 이동
    angle = tv.towards(tf.pos())
    tv.setheading(angle)
    tv.forward(7)

    # 추격자와 먹이가 닿았는지 체크
    if tv.distance(tf) < 20:
        game_over()
        return

    ontimer(play, 100)

# 키 입력 등록
def move():
    onkeypress(turn_right, "Right")
    onkeypress(turn_left, "Left")
    onkeypress(turn_up, "Up")
    onkeypress(turn_down, "Down")

# 시작
ready()
move_food()
move()
listen()
play()
mainloop()
