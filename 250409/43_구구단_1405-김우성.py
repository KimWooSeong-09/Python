# 43-1

for i in range(1, 10):
    print(' ')
    print(f'=={i}단==')
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j:>2}')

# 43-2

user_input = int(input("몇단 ? : "))

print(f'== {user_input}단 ==')
for i in range(1, 10):
    print(f'{user_input} * {i} = {user_input * i :> 2}')