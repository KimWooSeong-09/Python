fruit = []

while True:
    if len(fruit) == 5:
        print(f'더이상 추가가 불가합니다. 최종 리스트 : {fruit}')
        break
    else:
        user_input = input("추가할 과일 이름을 입력해주세요 : ")
        if user_input in fruit:
            print(f'{user_input}은 이미 리스트에 있습니다!')
        else:
            fruit.append(user_input)
print("프로그램 종료")