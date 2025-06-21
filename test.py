import random as r

user_input = list(map(int, input("숫자 3개 입력 (1~9) : ").split()))
random_list = r.sample(range(1, 10), 3)

S = 0  # 스트라이크 개수
B = 0  # 볼 개수

# 스트라이크 판별
if user_input[0] == random_list[0]:
    S += 1
if user_input[1] == random_list[1]:
    S += 1
if user_input[2] == random_list[2]:
    S += 1

# 볼 판별 (같은 숫자가 있지만 위치가 다를 경우)
if user_input[0] in random_list and user_input[0] != random_list[0]:
    B += 1
if user_input[1] in random_list and user_input[1] != random_list[1]:
    B += 1
if user_input[2] in random_list and user_input[2] != random_list[2]:
    B += 1

print(f'컴퓨터 리스트 : {random_list}, S : {S}, B : {B}')
