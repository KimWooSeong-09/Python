print('###방법1###')
num=1
while num<=100:
    print(f'현재 숫자는 {num}')
    num+=1
print('프로그램 종료')

print('###방법2###')
num1=1
while True:
    print(f'현재 숫자는 {num1}')
    num1+=1
    if num1>100:
        break
print('프로그램 종료')