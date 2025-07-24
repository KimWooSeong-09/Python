while True:
    try:
        user_input = int(input("숫자 : "))
    except ValueError:
        print("프로그램 종료")
        break
    else:
        if user_input != 0:
            if user_input % 5 == 0:
                print("5의 배수입니다.")
            else:
                print("5의 배수가 아닙니다.")
