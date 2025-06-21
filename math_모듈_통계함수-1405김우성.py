import math

# 평균
def f_avg(lst):
    return sum(lst) / len(lst)

# 분산
def f_var(lst, mean, x=0):
    if x == len(lst):
        return 0
    return (lst[x] - mean) ** 2 + f_var(lst, mean, x + 1)

# 표준편차
def f_std(var, n):
    return math.sqrt(var / n)

# 최대공약수
def f_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 최소공배수
def f_lcm(x, y):
    return x * y // f_gcd(x, y)

user_list = list(map(int, input("리스트에 들어갈 숫자 입력 : ").split()))
print(f'유저님의 리스트는 {user_list}입니다.')
mean = f_avg(user_list)
var_sum = f_var(user_list, mean)
variance = var_sum / len(user_list)
std_dev = f_std(var_sum, len(user_list))
gcd = f_gcd(max(user_list), min(user_list))
lcm = f_lcm(max(user_list), min(user_list))

print(f"평균: {mean}")
print(f"분산: {variance}")
print(f"표준편차: {std_dev}")
print(f"최대공약수 : {gcd}")
print(f"최소공배수 : {lcm}")
