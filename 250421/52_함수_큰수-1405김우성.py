def maxp(x, y):
    result = max(x, y)
    return result

# 인자 전달
print(f'큰 수 : {maxp(10, 20)}')

# 인자를 표준 입력 받아 전달
a, b = map(int, input("큰수 입력 : ").split())
print(f'큰 수 : {maxp(a, b)}')