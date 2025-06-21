juice_prize = 800
juice_count = 5

while True:
    if juice_count > 0:  
        print("=" * 20)
        user_input = int(input("돈을 넣어주세요(정수 형태만) : "))  
        if user_input > juice_prize:
            change = user_input - juice_prize
            print(f'맛있는 주스 드시고 잔돈 {change}원 받아 가세요.')
        elif user_input == juice_prize:
            print("맛있는 커피 드세요.")
        else:
            print("가격을 확인하세요.")
            print(user_input)
            continue
        juice_count -= 1
        print(f'남은 주스 갯수 : {juice_count}')
    else:
        print("주스가 매진되었습니다.")
        break
    