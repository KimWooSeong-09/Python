# 방법 1
num = 1
while num <= 60:
    print(f'현재 숫자는 {num}')
    num = num + 1
print("프로그램 종료")

# 방법 2
num = 1
while True:
    print(f'현재 숫자는 {num}')
    num += 1
    break
print("프로그램 종료")