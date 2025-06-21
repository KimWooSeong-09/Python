import random as r

com_list = [0, 0]
com_list[0] = r.choice([1, 2, 3, 4, 5, 6])  # 첫 번째 값 선택
com_list[1] = r.choice([1, 2, 3, 4, 5, 6])  # 두 번째 값 선택

user_input = map(int, input().split())
user_input = list(user_input)

com_list = [com_list[0], com_list[1]]
random_choice = r.choice(com_list[0]) # 저장

if random_choice in com_list:
    random_choice2 = r.choice(com_list[1])
    if random_choice2 in com_list:
        print("1등")
    else:
        print("2등")
else:
    print("3등")