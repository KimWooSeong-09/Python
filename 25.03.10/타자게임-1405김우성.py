import random as r
import time

word_list = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']

correct_count = 0
question_count = 1

input(" 타자 게임을 시작하려면 엔터를 누르세요!")

start_time = time.time() 
question = r.choice(word_list)

while correct_count < 5:
    print(f'[문제 {question_count}]')
    print(question)
    user_input = input(">>> ")

    if user_input == question:
        question = r.choice(word_list)
        print("PASS\n")
        correct_count += 1
    else:
        print("FAIL\n")
    
    question_count += 1

end_time = time.time() 
total_time = round(end_time - start_time, 2)

print(f"게임 완료! 총 소요 시간: {total_time}초")
