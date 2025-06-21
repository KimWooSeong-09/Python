while True:
    try:
        user_input = int(input("숫자를 입력하세요 : "))
    except ValueError:
        print("정수를 입력해주세요.")
    else:
        print(user_input)
        break