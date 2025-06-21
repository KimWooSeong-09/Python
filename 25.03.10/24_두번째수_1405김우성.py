number_list = [0] * 3
number_list[0], number_list[1], number_list[2] = map(int, input("세 수를 입력하세요:").split())
number_list.sort()
print(f'두번째 수는 {number_list[1]}입니다.')