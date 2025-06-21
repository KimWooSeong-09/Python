a = 1

while a != 0:
    a = int(input())
    if a != 0:
        if a % 5 == 0:
            print("5의 배수입니다.")
        else:
            print("5의 배수가 아닙니다.")
print("프로그램 종료")