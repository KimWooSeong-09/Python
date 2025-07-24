# 합계 함수 정의
def fun_s(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

# MAIN
print(fun_s(10))
print(fun_s(100))
print(fun_s(1000))

# 51-2

def fun_fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

# MAIN
print(fun_fact(5))
print(fun_fact(10))

# 재귀 함수

k = int(input("팩토리얼 : "))
def f(c):
    s = 1
    if c <= 1:
        return 1
    else:
        s = c * f(c - 1)
        return s

print(f(k))
    