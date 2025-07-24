com = ['가위', '바위', '보'] # 리스트 생성

user = input("가위 바위 보! :") # 입력

import random as r # 모듈

com_answer = r.choice(com) # 랜덤으로 저장
print(f"컴퓨터: {com_answer}")

# 계산
if user == com_answer:
    print("무승부!")
elif (user == '가위' and com_answer == '보') or (user == '바위' and com_answer == '가위') or (user == '보' and com_answer == '바위'):
    print("승리!")
else:
    print("패배!")