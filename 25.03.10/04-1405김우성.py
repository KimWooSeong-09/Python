# 입출력을 이용햔 BMI 계산 프로그램
# bmi = 
print("#" * 30)
print("      BMI 계산 프로그램")
print("#" * 30)
a = float(input("키(cm) : "))
b = float(input("몸무게(kg) : "))
print("#" * 30)

bmi = round(b / ((a / 100) ** 2), 1)
print(f'당신의 BMI지수는 {bmi}입니다.')