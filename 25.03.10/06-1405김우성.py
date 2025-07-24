# 원리합계 프로그램

print("[ 주의 ] 공백을 기준으로 입력할것. 예) 3 6 ")
m = int(input("돈 입력 : "))
rate, d = map(float, input("이율, 기간 입력 : ").split())

print("#" * 30)
result = m + (m * rate * 0.01 * d)
result = int(result)
print(f'{m}원을 {rate}% 이율로 {d}년간 예치 후 원리합계는 {result}원입니다.')
