# 39-1
user_input = int(input("자연수 : "))

sum = 0
for i in range(1, user_input + 1):
    sum += i

print(f'1부터 {user_input}까지의 합은 {sum}')

# 39-2
user_input = int(input("자연수 : "))

result = 1
for i in range(user_input, 0, -1):
    result = result * i
print(f'{user_input}!은 {result}')