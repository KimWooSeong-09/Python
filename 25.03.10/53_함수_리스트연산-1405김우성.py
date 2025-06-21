print("*** 리스트 생성")
user_list = list(map(float, (input("숫자(공백으로 분리) : ").split())))

while True:
    try:
        user_input = float(input("추가 숫자 : "))
        user_list.append(user_input)
    except ValueError:
        break


def num_s(x):
    number_sum = sum(x)
    return number_sum

def num_a(x, y):
    number_avg = x / y
    return number_avg

def lst_print(x, y):
    print("*** 계산 결과")
    print(f'점수 : {user_list}') 
    print(f'합계 : {x} | 평균 : {y}')

num_sum = num_s(user_list)
num_avg = num_a(num_sum, len(user_list))

lst_print(num_sum, num_avg)

